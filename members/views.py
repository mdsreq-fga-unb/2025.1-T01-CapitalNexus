from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required 
from .models import *
from .forms import FaltaForm, ReuniaoForm

@login_required
def home(request):
    proximas_reunioes = Reuniao.objects.filter(data_hora__gte=timezone.now()).order_by('data_hora')[:3]
    ultimas_atas = Reuniao.objects.filter(data_hora__gte=timezone.now()).exclude(ata='').order_by('data_hora')[:3]

    contexto = {
        'proximas_reunioes': proximas_reunioes,
        'ultimas_atas': ultimas_atas,
    }
    return render(request, 'members/home.html', contexto)

@login_required
def pagina_reunioes(request):
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
    }
    return render(request, 'members/reunioes.html', contexto)

@login_required
def editar_reuniao(request, reuniao_id):
    reuniao = get_object_or_404(Reuniao, id=reuniao_id)

    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES, instance = reuniao)
        if form.is_valid():
            form.save()
            messages.success(request, 'A reunião foi atualizada com sucesso!')
            return redirect('reunioes')
    else:
        form = ReuniaoForm(instance=reuniao)

    contexto = {
        'form': form,
        'reuniao': reuniao,
    }
    return render(request, 'members/editar_reuniao.html', contexto)


@login_required
def fazer_chamada(request, reuniao_id):
    
    reuniao = Reuniao.objects.get(id=reuniao_id)
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
            return redirect('reunioes')
    else:
        # Prepara o formset, um para cada membro
        initial_data = [{'membro_matricula': membro.matricula} for membro in membros]
        formset = FaltaFormSet(initial=initial_data)

    contexto = {
        'reuniao': reuniao,
        'formset': formset,
        'membros_e_forms': zip(membros, formset) # 'zip' para facilitar a vida no template
    }
    return render(request, 'members/chamada.html', contexto)

@login_required
def marcar_reuniao(request):
    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reunião marcada com sucesso!')
            return redirect('reunioes')
    
    messages.error(request, 'Houve um erro ao cadastrar a sua reunião. Veja se os dados informados estão no formato esperado e tente novamente.')
    return redirect('reunioes')
    

