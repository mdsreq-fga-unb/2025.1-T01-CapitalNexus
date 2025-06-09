from django.shortcuts import render
# from django.http import HttpResponse

def sobre(request):
    return render(request, 'public/sobre.html')

def projetos(request):
    return render(request, 'public/projetos.html')

def contato(request):
    return render(request, 'public/contato.html')
