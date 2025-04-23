from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Servidor

class ListaServidores(LoginRequiredMixin, ListView):
    model = Servidor
    template_name = 'inventario/lista.html'
    context_object_name = 'servidores'
    login_url = '/login/'  # ou você pode criar sua própria página
    ordering = ['hostname']

    def get_queryset(self):
        queryset = super().get_queryset()

        termo = self.request.GET.get('busca')
        if termo:
            queryset = queryset.filter(
                hostname__icontains=termo
            )

        ordenar = self.request.GET.get('ordenar')
        if ordenar:
            queryset = queryset.order_by(ordenar)

        return queryset

class CriarServidor(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Servidor
    fields = '__all__'
    template_name = 'inventario/formulario.html'
    success_url = reverse_lazy('lista_servidores')

class EditarServidor(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Servidor
    fields = '__all__'
    template_name = 'inventario/formulario.html'
    success_url = reverse_lazy('lista_servidores')

class DeletarServidor(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Servidor
    template_name = 'inventario/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_servidores')

