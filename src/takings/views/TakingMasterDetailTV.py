from time import time

from django.views.generic import TemplateView
from django.db import connection

from takings.lib import ConsolidateTaking
from accounts.mixins import ValidateManagerMixin


# /taking/detail/<int:pk>/
class TakingMasterDetailTV(ValidateManagerMixin, TemplateView):
    template_name = 'takings/taking-detail.html'

    def get(self, request, pk, *args, **kwargs):
        start_time = time()
        context = self.get_context_data(**kwargs)
        report = ConsolidateTaking().get(pk)

        page_data = {
            'title_page': 'Toma #{}'.format(pk),
            'module_name': 'Reporte de Toma',
            'taking': report['taking'],
            'report': report['report'],
            'warenhouses': report['warenhouses'],
            'enterprises': report['enterprises'],
            'total_time': time() - start_time,
        }
        return self.render_to_response(context={**context, **page_data})
