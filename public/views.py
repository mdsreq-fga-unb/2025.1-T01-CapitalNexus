from django.shortcuts import render
from .models import Projeto
# from django.http import HttpResponse

def sobre(request):
    return render(request, 'public/sobre.html')

def pagina_projetos(request):
    # Busca TODOS os objetos 'Projeto' do banco de dados
    todos_os_projetos = Projeto.objects.all()
    
    # Envia a lista de projetos para o template através do dicionário de contexto
    contexto = {
        'projetos': todos_os_projetos
    }
    return render(request, 'public/projetos.html', contexto)

def contato(request):
    return render(request, 'public/contato.html')
