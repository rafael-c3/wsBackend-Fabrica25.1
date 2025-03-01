from django import forms
from .models import Usuario

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
        