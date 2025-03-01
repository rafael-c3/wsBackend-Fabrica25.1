from django import forms
from .models import Usuario, Filme

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'nascimento', 'senha']
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'Email',
            'nascimento': 'Nascimento',
            'senha': 'Senha'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'nome': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'sobrenome': 'form-control'}),
            'email': forms.EmailInput(attrs={'sobrenome': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'nascimento': 'forms-control', 'type': 'date'}),
            'senha': forms.PasswordInput(attrs={'senha': 'form-control'}),
        }

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano']
        labels = {
            'titulo': 'Titulo',
            'ano': 'Ano',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'titulo': 'form-control'}),
            'ano': forms.DateInput(attrs={'ano': 'form-control'}),
        }