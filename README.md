comandos no terminal para iniciar um projeto DJANGO
django-admin startproject 'nome' .

Com o projeto criado, cria-se o App
python manage.py startapp 'nome'

LEMBRAR de adicionar no arquivo SETTINGS

ALLOWED_HOSTS = [
    '57fb-187-20-29-238.ngrok-free.app'
]

CSRF_TRUSTED_ORIGINS = [
    'https://57fb-187-20-29-238.ngrok-free.app'
]

