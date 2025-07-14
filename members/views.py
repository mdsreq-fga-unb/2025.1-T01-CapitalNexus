from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.forms import formset_factory
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse

from public.models import MensagemContato
from .models import *
from .forms import *

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
    else:
        form = JustificativaForm()
    
    messages.error(request, 'Houve um erro ao cadastrar suas justificativa. Veja se os dados informados estão no formato esperado e tente novamente.')
    return redirect('membros:faltaseadvertencias')

@login_required
def pagina_avaliar_justificativas(request):
    membro = Membro.objects.get(user=request.user)
    # 1. Busca todas as justificativas 
    justificativas = Justificativa.objects.select_related(
        'falta__reuniao', 'falta__membro__user'
    )

    # 2. Pega o ID da reunião da URL (ex: ?reuniao=5), se foi filtrado
    reuniao_id_filtro = request.GET.get('reuniao')

    status_filtro = request.GET.get('status')

    # 3. Aplica o filtro na nossa lista se um ID de reunião foi enviado
    if reuniao_id_filtro:
        # Filtra a lista para mostrar apenas justificativas daquela reunião
        justificativas = justificativas.filter(falta__reuniao__id=reuniao_id_filtro)
    if status_filtro:
        justificativas = justificativas.filter(status_analise=status_filtro)

    # 4. Pega uma lista de reuniões únicas para popular o dropdown do filtro
    reunioes = Reuniao.objects.all()

    contexto = {
        'justificativas': justificativas,
        'filtro_reunioes': reunioes,
        'membro': membro,
    }
    return render(request, 'members/justificativas.html', contexto)

@login_required
def processar_justificativa(request, just_id):
    # if not request.user.membro.is_gestor():
    #     return redirect('membros:home') # Segurança

    justificativa = get_object_or_404(Justificativa, id=just_id)

    if request.method == 'POST':
        decisao = request.POST.get('decisao') # Pega o valor do botão clicado ('ACEITA' ou 'REJEITADA')
        feedback = request.POST.get('feedback_analise')

        if decisao in ['ACEITA', 'REJEITADA']:
            justificativa.status_analise = decisao
            justificativa.feedback_analise = feedback
            

            justificativa.save()
            messages.success(request, f"A justificativa de {justificativa.falta.membro.nome} foi analisada.")
        
    return redirect('membros:justificativas')

@login_required
def pagina_gerenciar_advertencias(request):
    membro = Membro.objects.get(user=request.user)
    # if not request.user.membro.is_gestor():
    #     messages.error(request, "Você não tem permissão para acessar esta página.")
    #     return redirect('membros:home')
    advertencias_list = Advertencias.objects.all().prefetch_related('membro__membronucleo_set__nucleo')
    advertencias_list = Advertencias.objects.all()
    
    nucleo_query = request.GET.get('nucleo')
    membro_query = request.GET.get('membro')

    # Aplica os filtros se eles foram enviados
    if nucleo_query:
        # Filtra atravessando os relacionamentos: Advertencia -> Membro -> MembroNucleo -> Nucleo
        advertencias_list = advertencias_list.filter(membro__membronucleo__nucleo__nome=nucleo_query)
    
    if membro_query:
        advertencias_list = advertencias_list.filter(membro__nome__icontains=membro_query)

    # Buscamos todos os núcleos para popular o dropdown do filtro
    nucleos = Nucleo.objects.all()
    form_nova_advertencia = AdvertenciaForm()

    contexto = {
        'advertencias': advertencias_list,
        'nucleos_para_filtro': nucleos,
        'form_nova_advertencia': form_nova_advertencia,
        'membro': membro,
        'form_nova_advertencia': AdvertenciaForm(), # Para a modal
    }

    return render(request, 'members/advertencias.html', contexto)

@login_required
def registrar_advertencia(request):
    # if not request.user.membro.is_gestor():
    #     return redirect('membros:home')
    
    if request.method == 'POST':
        form = AdvertenciaForm(request.POST)
        if form.is_valid():
            advertencia = form.save(commit=False)
            advertencia.save()
            messages.success(request, 'Advertência registrada com sucesso.')
            return redirect('membros:advertencias')

    messages.error(request, 'Ocorreu um erro ao registrar a advertência. Verifique os dados e tente novamente.')
    return redirect('membros:advertencias')

@login_required
def editar_advertencia(request, advertencia_id):
    membro = Membro.objects.get(user=request.user)
    # Garante que apenas gestores podem editar
    # if not request.user.membro.is_gestor():
    #     messages.error(request, "Você não tem permissão para esta ação.")
    #     return redirect('membros:advertencias')

    # Busca a advertência específica ou retorna um erro 404
    advertencia = get_object_or_404(Advertencias, id=advertencia_id)

    if request.method == 'POST':
        # Se o formulário for enviado, preenchemos com os dados e a instância
        form = AdvertenciaForm(request.POST, instance=advertencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advertência atualizada com sucesso!')
            return redirect('membros:advertencias')
    else:
        # Se for a primeira visita, apenas mostramos o formulário preenchido
        form = AdvertenciaForm(instance=advertencia)

    contexto = {
        'form': form,
        'membro': membro,
    }
    return render(request, 'members/editar_advertencia.html', contexto)

@login_required
def excluir_advertencia(request, advertencia_id):
    membro = Membro.objects.get(user=request.user)
    # Garante que apenas gestores podem excluir
    # if not request.user.membro.is_gestor():
    #     messages.error(request, "Você não tem permissão para esta ação.")
    #     return redirect('dashboard-advertencias')

    advertencia = get_object_or_404(Advertencias, id=advertencia_id)

    # Se o formulário de confirmação foi enviado
    if request.method == 'POST':
        membro_nome = advertencia.membro.nome # Guarda o nome antes de deletar
        advertencia.delete() # Deleta o objeto do banco de dados
        messages.success(request, f"A advertência para {membro_nome} foi excluída com sucesso.")
        return redirect('membros:advertencias')

    # Se a página for apenas visitada (GET), mostra a página de confirmação
    contexto = {
        'advertencia': advertencia,
        'membro': membro,
    }
    return render(request, 'members/excluir_advertencia.html', contexto)

@login_required
def pagina_lista_de_materiais(request):
    membro = Membro.objects.get(user=request.user)
    # Começamos com todos os materiais
    queryset = Material.objects.all().select_related('nucleo_responsavel').prefetch_related('historico__membro')

    # Pega os valores dos filtros da URL (via request.GET)
    nucleo_tab_query = request.GET.get('nucleo')
    nome_query = request.GET.get('nome')
    tipo_query = request.GET.get('tipo')
    status_query = request.GET.get('status')
    
    # Aplica o filtro da ABA de núcleo
    if nucleo_tab_query and nucleo_tab_query != 'Todos os Núcleos':
        queryset = queryset.filter(nucleo_responsavel__nome=nucleo_tab_query)

    # Aplica os outros filtros
    if nome_query:
        queryset = queryset.filter(nome__icontains=nome_query)
    if tipo_query:
        queryset = queryset.filter(tipo=tipo_query)
    if status_query:
        queryset = queryset.filter(status=status_query)

    # Buscamos todos os núcleos para popular as abas de navegação
    nucleos = Nucleo.objects.all()

    contexto = {
        'membro': membro,
        'materiais': queryset,
        'nucleos_para_tabs': nucleos,
        'nucleo_ativo': nucleo_tab_query or 'Todos os Núcleos'
    }
    contexto['form_novo_material'] = MaterialForm()
    contexto['form_reserva'] = ReservaForm()
    contexto['form_solicitacao'] = SolicitacaoMaterialForm()
    return render(request, 'members/materiais.html', contexto)

@login_required
def novo_material(request):
    # if not request.user.membro.is_gestor():
    #     return redirect('membros:materiais')
    
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo material cadastrado com sucesso!')
        else:
            messages.error(request, 'Houve um erro ao cadastrar o material. Verifique os dados e tente novamente.')
    return redirect('membros:materiais')

def material_detalhes_api(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    # Transforma os dados do modelo em um formato que o JavaScript entende (JSON)
    dados = {
        'nome': material.nome, 'tipo': material.tipo, 'finalidade': material.finalidade,
        'quantidade_total': material.quantidade_total, 'status': material.status,
        # 'em_uso_por_id': material.em_uso_por.user.id if material.em_uso_por else '',
        'nucleo_responsavel_id': material.nucleo_responsavel.id if material.nucleo_responsavel else '',
    }
    return JsonResponse(dados)

@login_required
def editar_material(request, material_id):
    # if not request.user.membro.is_gestor():
    #     return redirect('membros:materiais')
    
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material atualizado com sucesso!')
        else:
            messages.error(request, 'Houve um erro ao atualizar. Verifique os dados.')
    return redirect('membros:materiais')

@login_required
def reservar_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    membro = get_object_or_404(Membro, user=request.user)

    if material.status != 'DISPONIVEL':
        messages.error(request, "Este material não está disponível para reserva.")
        return redirect('membros:materiais')

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Cria o registro no histórico
            reserva = form.save(commit=False)
            reserva.material = material
            reserva.membro = membro
            reserva.save()

            # Atualiza o status do material
            material.status = 'EM_USO'
            material.save()

            messages.success(request, f"Material '{material.nome}' reservado com sucesso!")
            return redirect('membros:materiais')

    # Se o formulário for inválido, redireciona com erro
    messages.error(request, "Houve um erro ao reservar o material. Verifique a data informada e tente novamente.")
    return redirect('membros:materiais')

@login_required
def devolver_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    
    # Apenas aceita a ação se for via POST (do formulário de confirmação)
    if request.method == 'POST':
        reserva_ativa = material.get_reserva_ativa()
        if reserva_ativa and (reserva_ativa.membro.user == request.user or request.user.membro.is_gestor()):
            # Atualiza o registro de histórico com a data de devolução
            reserva_ativa.data_devolucao_real = timezone.now()
            reserva_ativa.save()

            # Atualiza o status do material de volta para disponível
            material.status = 'DISPONIVEL'
            material.save()
            
            messages.success(request, f"Material '{material.nome}' devolvido com sucesso.")
        else:
            messages.error(request, "Não foi possível processar a devolução.")

    return redirect('membros:materiais')

@login_required
def marcar_material_disponivel(request, material_id):
    # Garante que apenas gestores podem executar esta ação
    # if not request.user.membro.is_gestor():
    #     messages.error(request, "Você não tem permissão para esta ação.")
    #     return redirect('membros:materiais')

    if request.method == 'POST':
        material = get_object_or_404(Material, id=material_id)
        material.status = 'DISPONIVEL'
        material.save()
        messages.success(request, f"O material '{material.nome}' foi marcado como disponível.")
    
    return redirect('membros:materiais')

@login_required
def solicitar_material(request):
    if request.method == 'POST':
        form = SolicitacaoMaterialForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            # Associamos o membro logado à solicitação
            solicitacao.solicitante = request.user.membro
            solicitacao.save()
            messages.success(request, 'Sua solicitação de material foi enviada para análise!')
        else:
            messages.error(request, 'Houve um erro no formulário. Verifique os dados.')
    return redirect('membros:materiais')

@login_required
def pagina_lista_membros(request):
    membro = Membro.objects.get(user=request.user)
    # Começamos com todos os membros
    membros = (
        Membro.objects.all()
        .order_by('nome') 
        .select_related('user')
        .prefetch_related('membronucleo_set__nucleo', 'membronucleo_set__cargo')
    )

    # Pegamos os valores dos filtros da URL
    nome_query = request.GET.get('nome')
    cargo_query = request.GET.get('cargo')
    nucleo_query = request.GET.get('nucleo')

    # Aplicamos os filtros
    if nome_query:
        membros_list = membros.filter(nome__icontains=nome_query)
    if cargo_query:
        membros_list = membros.filter(membronucleo__cargo__posicao=cargo_query)
    if nucleo_query:
        membros_list = membros.filter(membronucleo__nucleo__nome=nucleo_query)

    membros = membros.distinct()
    paginator = Paginator(membros, 15) # 15 mensagens por página
    page_number = request.GET.get('page')
    membros_list = paginator.get_page(page_number)

    # Buscamos todos os cargos e núcleos para popular os dropdowns dos filtros
    todos_cargos = Cargo.objects.all()
    todos_nucleos = Nucleo.objects.all()

    contexto = {
        'membros': membros_list,
        'cargos_para_filtro': todos_cargos,
        'nucleos_para_filtro': todos_nucleos,
        'membro': membro,
    }
    contexto['form_novo_membro'] = NovoMembroForm()
    return render(request, 'members/membros.html', contexto)

@login_required
def membro_novo(request):
    # if not request.user.membro.is_gestor():
    #     return redirect('members:membros')

    if request.method == 'POST':
        form = NovoMembroForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            try:
                # 1. Cria o User
                novo_user = User.objects.create_user(
                    username=dados['username'],
                    password=dados['password'],
                    email=dados['email'],
                    first_name=dados['first_name'],
                    last_name=dados['last_name']
                )
                # 2. Cria o Membro, ligando-o ao User
                novo_membro = Membro.objects.create(
                    user=novo_user,
                    matricula=dados['matricula'],
                    nome=f"{dados['first_name']} {dados['last_name']}",
                    email=dados['email']
                )
                # 3. Cria a associação entre Membro e Núcleo/Cargo
                MembroNucleo.objects.create(
                    membro=novo_membro,
                    nucleo=dados['nucleo'],
                    cargo=dados['cargo']
                )
                messages.success(request, f"Membro '{novo_membro.nome}' adicionado com sucesso!")
                return redirect('membros:membros')
            except Exception as e:
                messages.error(request, f"Ocorreu um erro: {e}")
    
    return redirect('membros:membros')

@login_required
def membro_editar(request, matricula):
    # if not request.user.membro.is_gestor():
    #     messages.error(request, "Você não tem permissão.")
    #     return redirect('membros:membros')
    membro = get_object_or_404(Membro, matricula=matricula)

    if request.method == 'POST':
        form = EditarMembroForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            
            # --- LÓGICA DE SALVAMENTO ATUALIZADA ---
            user = membro.user
            user.email = dados['email'] # O email ainda pertence ao User
            user.save()

            # Agora atualizamos o nome diretamente no objeto Membro
            membro.nome = dados['nome']
            membro.email =dados['email']
            membro.save()
            # --- FIM DA LÓGICA DE SALVAMENTO ---

            # Lógica para atualizar associações de núcleo e cargo (continua a mesma)
            membro.membronucleo_set.all().delete()
            for nucleo in dados['nucleos']:
                MembroNucleo.objects.create(membro=membro, nucleo=nucleo, cargo=dados['cargo'])
            
            messages.success(request, f"Dados de {membro.nome} atualizados com sucesso!")
            return redirect('membros:membros')
    else:
        # --- LÓGICA DE PREENCHIMENTO ATUALIZADA ---
        associacoes = membro.membronucleo_set.all()
        initial_data = {
            'nome': membro.nome, # Usamos o nome do Membro
            'email': membro.user.email,
            'matricula': membro.matricula,
            'cargo': associacoes.first().cargo if associacoes.exists() else None,
            'nucleos': [assoc.nucleo for assoc in associacoes],
        }
        form = EditarMembroForm(initial=initial_data)

    contexto = {'form': form, 'membro': membro}
    return render(request, 'members/editar_membro.html', contexto)

@login_required
def membro_excluir(request, matricula):
    # if not request.user.membro.is_gestor():
    #     messages.error(request, "Você não tem permissão.")
    #     return redirect('membros:membros')

    membro = get_object_or_404(Membro, matricula=matricula)
    if request.method == 'POST':
        user = membro.user
        user.delete() # Ao deletar o User, o Membro e outras associações com CASCADE serão deletados
        messages.success(request, f"Membro '{membro.nome}' foi excluído com sucesso.")
        return redirect('membros:membros')

    return render(request, 'members/excluir_membro.html', {'membro': membro})

@login_required
def pagina_painel_administrativo(request):
    if not request.user.membro.is_gestor():
        messages.error(request, "Você não tem permissão.")
        return redirect('membros:home')
    
    # Busca todas as mensagens, ordenando pelas mais novas
    mensagens_list = MensagemContato.objects.all().order_by('-data_envio')
    
    # Adiciona paginação para não sobrecarregar a tela
    paginator = Paginator(mensagens_list, 15) # 15 mensagens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    contexto = {
        'nucleos': Nucleo.objects.all(),
        'page_obj': page_obj,
    }
    return render(request, 'members/painel.html', contexto)

@login_required
def nucleo_editar(request, pk):
    # if not request.user.membro.is_gestor():
    #     return redirect('membros:membros')
    
    nucleo = get_object_or_404(Nucleo, pk=pk)
    if request.method == 'POST':
        form = NucleoForm(request.POST, instance=nucleo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Núcleo atualizado com sucesso!')
            return redirect('membros:painel')
    else:
        form = NucleoForm(instance=nucleo)
        
    contexto = {'form': form, 'nucleo': nucleo}
    return render(request, 'members/editar_nucleo.html', contexto)

@login_required
def marcar_mensagem_lida(request, mensagem_id):
    # Garante que apenas gestores podem executar a ação
    if not request.user.membro.is_gestor():
        return JsonResponse({'status': 'error', 'message': 'Não autorizado'}, status=403)
    
    # Apenas aceita requisições POST por segurança
    if request.method == 'POST':
        mensagem = get_object_or_404(MensagemContato, id=mensagem_id)
        if not mensagem.lido:
            mensagem.lido = True
            mensagem.save()
        return JsonResponse({'status': 'ok'})
    
    return JsonResponse({'status': 'error', 'message': 'Requisição inválida'}, status=400)