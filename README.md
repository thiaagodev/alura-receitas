# Alura Receitas

O Alura receitas é uma aplicação que foi desenvolvida ao longo de cursos da formação Django da Alura.

https://cursos.alura.com.br/formacao-django


### Como executar o projeto

- Clone o repositório e crie uma virtual env no diretório raiz.
- Ative a venv com "source ./venv/bin/activate" se estiver no Linux, caso seja Windows o comando é "./venv/scripts/activate".
- Para instalar as libs necessárias use o comando "pip install -r requirements.txt"
- Rode as migrations com o comando "python manage.py migrate"
- Crie um arquivo .env com as informações do banco de dados, ou use o padrão Sqlite.
- Rode o servidor com o comando "python3 manage.py runserver"
