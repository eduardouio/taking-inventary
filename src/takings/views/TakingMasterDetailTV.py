from django.views.generic import TemplateView

from takings.models import Taking, TakinDetail
from django.accounts.mixins import ValidateManagerMixin


# /taking/detail/<int:pk>/
class TakingMasterDetailTV(ValidateManagerMixin, TemplateView):
    template_name='takings/taking-detail.html'

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        taking = Taking.get(pk)
        taking_detail = TakinDetail.get_by_taking(pk)
        page_data = {
            'title_page': 'Detalle Toma {}'.format(pk) ,
            'taking': taking,
            'taking_detail': taking_detail,
            'module_name': 'Toma',
        }
        return self.render_to_response(context={**context, **page_data})