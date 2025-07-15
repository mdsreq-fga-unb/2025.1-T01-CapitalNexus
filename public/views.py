from django.shortcuts import render, redirect
from .models import Projeto, MensagemContato, Patrocinador
from .forms import FormularioContato
from django.contrib import messages

def sobre(request):
    """
    View responsável por exibir a página 'Sobre', incluindo a lista de patrocinadores.
    Busca todos os objetos da model Patrocinador e os envia ao template.

    Args:
        request (HttpRequest): Objeto da requisição HTTP.

    Returns:
        HttpResponse: Página HTML renderizada com a lista de patrocinadores.
    """
    lista_de_patrocinadores = Patrocinador.objects.all()
    contexto = {
        'patrocinadores': lista_de_patrocinadores
    }
    return render(request, 'public/sobre.html', contexto)

def pagina_projetos(request):
    """
    View responsável por exibir a página com os projetos públicos.
    Busca todos os objetos da model Projeto e os envia ao template.

    Args:
        request (HttpRequest): Objeto da requisição HTTP.

    Returns:
        HttpResponse: Página HTML renderizada com a lista de projetos.
    """
    lista_de_projetos = Projeto.objects.all()
    contexto = {
        'projetos': lista_de_projetos
    }
    return render(request, 'public/projetos.html', contexto)

def pagina_contato(request):
    """
    View responsável por exibir e processar o formulário de contato.

    Se o método da requisição for POST, os dados enviados pelo usuário são validados
    e salvos no banco de dados como uma nova mensagem. Em seguida, o usuário é redirecionado
    com uma mensagem de sucesso. Se for GET, exibe o formulário em branco.

    Args:
        request (HttpRequest): Objeto da requisição HTTP, contendo método e dados do usuário.

    Returns:
        HttpResponse: Página HTML renderizada com o formulário ou redirecionamento após envio.
    """
    if request.method == 'POST':
        form = FormularioContato(request.POST)
        if form.is_valid():
            MensagemContato.objects.create(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                mensagem=form.cleaned_data['mensagem']
            )
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Responderemos em breve.')
            return redirect('publico:contato')
    else:
        form = FormularioContato()

    contexto = {
        'form': form
    }
    return render(request, 'public/contato.html', contexto)
