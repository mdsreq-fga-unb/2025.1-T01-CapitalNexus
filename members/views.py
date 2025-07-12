from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required 
from .models import *
from .forms import FaltaForm, JustificativaForm, ReuniaoForm

@login_required
def home(request):
    """
    View responsável pela página inicial da área dos membros.

    Pega as informações do membro logado, além de susas faltas e advertências
    para os cards do template.

    Args:
        request (HttpRequest): Objeto da requisição HTTP.

    Returns:
        HttpResponse: Página HTML renderizada com a lista de projetos.
    """
    contexto = {} 

    try:
        membro_logado = Membro.objects.get(user=request.user)
        minhas_faltas = Falta.objects.filter(membro=membro_logado)
        minhas_advertencias = Advertencias.objects.filter(membro=membro_logado)
        
        total_faltas = minhas_faltas.count()
        total_advertencias = minhas_advertencias.count()

        contexto['minhas_faltas'] = minhas_faltas
        contexto['minhas_advertencias'] = minhas_advertencias
        contexto['total_faltas'] = total_faltas
        contexto['total_advertencias'] = total_advertencias
        contexto['membro'] = membro_logado
        ultimas_atas = Reuniao.objects.filter(data_hora__lt=timezone.now()).exclude(ata='').order_by('-data_hora')[:3] 
        contexto['ultimas_atas'] = ultimas_atas
    except Membro.DoesNotExist:
        pass

    contexto['proximas_reunioes'] = Reuniao.objects.filter(data_hora__gte=timezone.now()).order_by('data_hora')[:3]

    return render(request, 'members/home.html', contexto)

@login_required
def pagina_reunioes(request):
    membro = Membro.objects.get(user=request.user)
    queryset = Reuniao.objects.all().order_by('-data_hora')

    # Pegamos os valores dos filtros da URL (via request.GET)
    titulo_query = request.GET.get('titulo')
    tipo_query = request.GET.get('tipo')
    data_query = request.GET.get('data')

    # Aplicamos os filtros um por um, se eles existirem
    if titulo_query:
        queryset = queryset.filter(titulo__icontains=titulo_query)
    
    if tipo_query:
        queryset = queryset.filter(tipo=tipo_query)

    if data_query:
        queryset = queryset.filter(data_hora__date__gte=data_query)

    form_nova_reuniao = ReuniaoForm()

    contexto = {
        'reunioes': queryset, # Enviamos a lista já filtrada
        'form_nova_reuniao': form_nova_reuniao,
        'membro': membro,
    }
    return render(request, 'members/reunioes.html', contexto)

@login_required
def editar_reuniao(request, reuniao_id):
    """
    View para editar uma reunião existente.

    Obtém a reunião pelo ID ou retorna 404 se não encontrada.
    Se o método da requisição for POST, valida e salva as alterações no formulário.
    Em caso de sucesso, adiciona uma mensagem e redireciona para a lista de reuniões.
    Se for GET, exibe o formulário preenchido com os dados atuais da reunião.

    Args:
        request (HttpRequest): Objeto da requisição HTTP.
        reuniao_id (int): ID da reunião a ser editada.

    Returns:
        HttpResponse: Página com o formulário de edição ou redirecionamento após salvar.
    """
    membro = Membro.objects.get(user=request.user)
    reuniao = get_object_or_404(Reuniao, id=reuniao_id)

    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES, instance = reuniao)
        if form.is_valid():
            form.save()
            messages.success(request, 'A reunião foi atualizada com sucesso!')
            return redirect('membros:reunioes')
    else:
        form = ReuniaoForm(instance=reuniao)

    contexto = {
        'form': form,
        'reuniao': reuniao,
        'membro': membro,
    }
    return render(request, 'members/editar_reuniao.html', contexto)

@login_required
def fazer_chamada(request, reuniao_id):
    """
    View para registrar a lista de presença (chamada) de uma reunião.

    Verifica se já existe uma lista de faltas para a reunião; caso positivo,
    exibe uma mensagem de aviso e redireciona. Se não, exibe um formset para marcar
    quem faltou.

    No método POST, processa o formset para criar ou apagar registros de faltas
    conforme os checkboxes selecionados.

    Args:
        request (HttpRequest): Objeto da requisição HTTP.
        reuniao_id (int): ID da reunião para a qual a chamada será feita.

    Returns:
        HttpResponse: Renderiza o formulário de chamada ou redireciona após salvar.
    """
    membro = Membro.objects.get(user=request.user)
    reuniao = Reuniao.objects.get(id=reuniao_id)

    if Falta.objects.filter(reuniao=reuniao).exists():
        messages.warning(request, "Já foi cadastrada uma lista de presença para essa reunião! Confire os faltantes em Faltas e Advertências")
        return redirect('membros:reunioes')

    membros = Membro.objects.all().order_by('nome')
    FaltaFormSet = formset_factory(FaltaForm, extra=0)

    if request.method == 'POST':
        formset = FaltaFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                dados = form.cleaned_data
                membro_matricula = dados.get('membro_matricula')
                faltou = dados.get('faltou')
                
                if membro_matricula:
                    membro = Membro.objects.get(matricula=membro_matricula)
                    # Se o checkbox foi MARCADO, apaga registro de falta.
                    if faltou:
                        Falta.objects.filter(reuniao=reuniao, membro=membro).delete()
                    # Se não foi marcado, cria a falta caso ela não exista.
                    else:
                        Falta.objects.get_or_create(reuniao=reuniao, membro=membro)
            
            messages.success(request, f"Faltas para a reunião '{reuniao.titulo}' foram salvas.")
            return redirect('membros:reunioes')
    else:
        # Prepara o formset, um para cada membro
        initial_data = [{'membro_matricula': membro.matricula} for membro in membros]
        formset = FaltaFormSet(initial=initial_data)

    contexto = {
        'reuniao': reuniao,
        'formset': formset,
        'membros_e_forms': zip(membros, formset), # 'zip' para facilitar a vida no template
        'membro': membro,
    }
    return render(request, 'members/chamada.html', contexto)

@login_required
def marcar_reuniao(request):
    """
    View para marcar (criar) uma nova reunião.

    No método POST, valida os dados do formulário e salva a nova reunião.
    Exibe mensagem de sucesso e redireciona para a lista de reuniões.
    Caso haja erro no formulário, exibe mensagem de erro e redireciona.

    Args:
        request (HttpRequest): Objeto da requisição HTTP.

    Returns:
        HttpResponseRedirect: Redirecionamento para a lista de reuniões.
    """
    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reunião marcada com sucesso!')
            return redirect('membros:reunioes')
    
    messages.error(request, 'Houve um erro ao cadastrar a sua reunião. Veja se os dados informados estão no formato esperado e tente novamente.')
    return redirect('membros:reunioes')

@login_required
def pagina_faltas_advertencias(request):
    contexto = {
        'minhas_faltas': Falta.objects.none(),
        'minhas_advertencias': Advertencias.objects.none(),
        'total_faltas': 0,
        'total_advertencias': 0
    }

    try:
        membro_logado = Membro.objects.get(user=request.user)

        # Primeiro, calculamos os totais, antes de qualquer filtro
        total_faltas = Falta.objects.filter(membro=membro_logado).count()
        total_advertencias = Advertencias.objects.filter(membro=membro_logado).count()

        # Adicionamos os totais ao contexto
        contexto['total_faltas'] = total_faltas
        contexto['total_advertencias'] = total_advertencias

        # Pegamos o valor do filtro da URL
        tipo_filtro = request.GET.get('tipo', 'todos')

        # Filtramos as listas com base na escolha do usuário
        if tipo_filtro == 'todos':
            faltas_filtradas = Falta.objects.filter(membro=membro_logado).select_related('reuniao', 'justificativa')
            advertencias_filtradas = Advertencias.objects.filter(membro=membro_logado)
        elif tipo_filtro == 'falta':
            faltas_filtradas = Falta.objects.filter(membro=membro_logado).select_related('reuniao', 'justificativa')
            advertencias_filtradas = Advertencias.objects.none() # Retorna uma lista vazia
        elif tipo_filtro == 'advertencia':
            faltas_filtradas = Falta.objects.none() # Retorna uma lista vazia
            advertencias_filtradas = Advertencias.objects.filter(membro=membro_logado)
        
        contexto['minhas_faltas'] = faltas_filtradas
        contexto['minhas_advertencias'] = advertencias_filtradas
        contexto['form_justificativa'] = JustificativaForm()
        contexto['membro'] = membro_logado

    except Membro.DoesNotExist:
        pass

    return render(request, 'members/faltaseadvertencias.html', contexto)

@login_required
def justificar_falta(request, falta_id):
    # Encontra a falta específica que o usuário está tentando justificar
    falta = get_object_or_404(Falta, id=falta_id, membro__user=request.user)

    # Verifica se já não existe uma justificativa para esta falta
    if hasattr(falta, 'justificativa'):
        messages.error(request, "Esta falta já foi justificada.")
        return redirect('membros:faltaseaqdvertencias')

    if request.method == 'POST':
        form = JustificativaForm(request.POST)
        if form.is_valid():
            nova_justificativa = form.save(commit=False) # Cria o objeto, mas não salva ainda
            nova_justificativa.falta = falta # Associa a justificativa à falta correta
            nova_justificativa.save() # Salva no banco de dados
            messages.success(request, "Sua justificativa foi enviada para análise.")
            return redirect('membros:faltaseadvertencias')
    
    messages.error(request, 'Houve um erro ao cadastrar suas justificativa. Veja se os dados informados estão no formato esperado e tente novamente.')
    return redirect('membros:faltaseadvertencias')