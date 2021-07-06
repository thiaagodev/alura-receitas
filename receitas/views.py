from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.order_by('-data').filter(publicada=True)
    dados = {
        'receitas': receitas
    }
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    dados = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', dados)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = Receita.objects.order_by('-data').filter(publicada=True, nome__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)
