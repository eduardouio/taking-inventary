from django.views.generic import ListView
from accounts.mixins import ValidateManagerMixin
from takings.models import Taking


# /taking/list/
class TakingsList(ListView):
    template_name = 'takings/list-takings.html'
    model = Taking

    def get(self, request, *args, **kwargs):
        # Obtener la lista de libros
        self.object_list = self.get_queryset()

        # Agregar algunos datos adicionales al contexto
        extra_context = {
            'title_page': 'Lista de Tomas',
            'some_data': 123,
        }
        context = self.get_context_data(**kwargs)
        # Devolver la respuesta
        return self.render_to_response({**context, **extra_context})