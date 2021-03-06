from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from receitas.models import Receita

# Create your views here.
def index(request):
    """ Retorna uma página mostrando todas as receitas publicadas com paginação """
    receitas = Receita.objects.order_by('-data').filter(publicada=True)
    paginator = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    """ Retorna os detalhes de uma determinada receita dado o seu id """
    receita = get_object_or_404(Receita, pk=receita_id)
    dados = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', dados)

def cria_receita(request):
    """ Recebe os dados e cria uma nova receita """
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(pessoa=user, nome=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_de_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto=foto_receita)
        receita.save()

        return redirect('dashboard')
    else:      
        return render(request, 'receitas/cria_receita.html')

def deleta_receita(request, receita_id):
    """ Deleta uma receita """
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    messages.success(request, f'A receita {receita.nome} foi delatada com sucesso!')
    return redirect('dashboard')

def edita_receita(request, receita_id):
    """ Retorna um formulário para edição de uma determinada receita dado o seu id """
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_editar = {
        'receita': receita
    }
   
    return render(request, 'receitas/edita_receita.html', receita_editar)

def atualiza_receita(request):
    """ Atualiza de fato a receita após ter sido editada """
    if request.method == 'POST':
        receita_id = request.POST['receita_id']

        receita = Receita.objects.get(pk=receita_id)
        receita.nome = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_de_preparo = request.POST['tempo_preparo']
        receita.rendimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']

        if 'foto_receita' in request.FILES:
            receita.foto = request.FILES['foto_receita']
        
        receita.save()
        messages.success(request, f'Receita {receita.nome} atualizada com sucesso!')
        return redirect('dashboard')
