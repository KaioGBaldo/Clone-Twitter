import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

# ---> ADICIONE ESTAS LINHAS PARA FAZER A VERCEL CRIAR AS TABELAS SOZINHA:
from django.core.management import call_command
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Erro ao rodar migrações: {e}")
# <---

app = application
