from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    nascimento = models.DateField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=30)
    ano = models.DateField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo