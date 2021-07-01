from django.contrib import admin
from .models import Receita

class LisReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'tempo_de_preparo' ,'data', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Receita, LisReceitas)
