from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BuscaForm
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def add_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Cadastrar Autor'})

def add_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Cadastrar Categoria'})

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Cadastrar Post'})

def buscar_post(request):
    resultado = None
    if request.method == "POST":
        form = BuscaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultado = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscaForm()
    return render(request, 'blog/busca.html', {'form': form, 'resultado': resultado})
