from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'autor', 'categoria']

# Formulário de busca
class BuscaForm(forms.Form):
    titulo = forms.CharField(label='Buscar Post pelo Título', max_length=200)
