from django.contrib import admin
from .models import Receita

class LisReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'tempo_de_preparo' ,'data')
    list_display_links = ('id', 'nome')

admin.site.register(Receita, LisReceitas)
