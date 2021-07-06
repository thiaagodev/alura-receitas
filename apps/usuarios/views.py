from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """ Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O nome não pode ser em branco!')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O email não pode ser em branco!')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de um usuário no sistema """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco!')
            return redirect('login')
        
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'O usuário não existe!')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def logout(request):
    """ Realiza o logout do usuário logado (sair da conta) """
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """ Retorna a página de dashboard do usuário, com suas próprias receitas """
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    """ Verifica se um determinado campo é vazio e retorna True ou False """
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    """ Verifica se duas senhas são exatemente iguais, caso sim retorna True """
    return senha != senha2