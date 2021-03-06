from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
