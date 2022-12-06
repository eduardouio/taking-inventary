from django.views.generic import TemplateView
from common import loggin


# /taking/detail/<int:pk>/
class TakingMasterDetailTV(TemplateView):
    template_name='takings/taking-detail.html'

    def get(self, request, pk, *args, **kwargs):
        loggin('i', 'mostrando detalles de toma')
        context = self.get_context_data(**kwargs)
        page_data = {
            'title_page': 'Detalle de Toma',
        }
        return self.render_to_response(context={**context, **page_data})