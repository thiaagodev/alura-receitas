from django.db import models
from django.db.models.fields import TextField

class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
