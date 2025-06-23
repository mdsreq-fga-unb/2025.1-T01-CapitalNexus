from django.shortcuts import render, redirect
from .models import Projeto, MensagemContato, Patrocinador
from .forms import FormularioContato
# from django.http import HttpResponse

def sobre(request):
    lista_de_patrocinadores = Patrocinador.objects.all()
    contexto = {
        'patrocinadores': lista_de_patrocinadores
    }
    return render(request, 'public/sobre.html', contexto)

def pagina_projetos(request):
    # Busca TODOS os objetos 'Projeto' do banco de dados
    lista_de_projetos = Projeto.objects.all()
    
    # Envia a lista de projetos para o template através do dicionário de contexto
    contexto = {
        'projetos': lista_de_projetos
    }
    return render(request, 'public/projetos.html', contexto)

def pagina_contato(request):
    if request.method == 'POST':
        # Se o formulário foi enviado (método POST), processamos os dados
        form = FormularioContato(request.POST)
        if form.is_valid():
            # Se os dados são válidos, podemos trabalhar com eles
            MensagemContato.objects.create(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                mensagem=form.cleaned_data['mensagem']
            )
            
            return redirect('sucesso') # Redireciona para uma página de sucesso
    else:
        # Se for a primeira vez na página (método GET), apenas exibe um formulário em branco
        form = FormularioContato()

    contexto = {
        'form': form
    }
    return render(request, 'public/contato.html', contexto)

# View para a página de sucesso
def pagina_sucesso(request):
    return render(request, 'public/sucesso.html')
