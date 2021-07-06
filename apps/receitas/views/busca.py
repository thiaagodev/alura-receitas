from django.shortcuts import render
from receitas.models import Receita


def busca(request):
    """ Busca uma receita pelo seu nome """
    lista_receitas = Receita.objects.order_by('-data').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = Receita.objects.order_by('-data').filter(publicada=True, nome__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)