from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    nascimento = models.DateField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return (self.nome + " " + self.sobrenome)