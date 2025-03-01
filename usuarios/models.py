from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    nascimento = models.DateField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return (self.nome + " " + self.sobrenome)
    
class Filme(models.Model):
    titulo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo