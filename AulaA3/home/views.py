from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livro

def home(request):
    return render(request, 'home.html')


def cadastrar(request):
    if request.method == 'POST':
        Livro.objects.create(
            titulo=request.POST['titulo'],
            autor=request.POST['autor'],
            editora=request.POST['editora'],
            ano=request.POST['ano'],
            paginas=request.POST['paginas'],
            categoria=request.POST['categoria'],
            isbn=request.POST['isbn'],
            idioma=request.POST['idioma'],
            descricao=request.POST['descricao'],
            cadastrado_por=request.POST['cadastrado_por']
        )
        return render(request, 'confirmar_cadastro.html')

    return render(request, 'cadastrar.html')


def consulta(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        livros = Livro.objects.filter(titulo__icontains=nome)
        return render(request, 'resultado_consulta.html', {'livros': livros})

    return render(request, 'consulta.html')


def listar(request):
    livros = Livro.objects.all()
    return render(request, 'listar.html', {'livros': livros})


def detalhe(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'detalhe.html', {'livro': livro})


def excluir(request, id):
    livro = Livro.objects.get(id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('listar')

    return render(request, 'confirmar_exclusao.html', {'livro': livro})


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')

# Create your views here.
