from waitress import serve
from gestao_servidores.wsgi import application

serve(application, host='0.0.0.0', port=8000)