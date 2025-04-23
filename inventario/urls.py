from django.urls import path
from .views import ListaServidores, CriarServidor, EditarServidor, DeletarServidor


urlpatterns = [
    path('', ListaServidores.as_view(), name='lista_servidores'),
    path('novo/', CriarServidor.as_view(), name='criar_servidor'),
    path('editar/<int:pk>/', EditarServidor.as_view(), name='editar_servidor'),
    path('deletar/<int:pk>/', DeletarServidor.as_view(), name='deletar_servidor'),
]


"""

"""