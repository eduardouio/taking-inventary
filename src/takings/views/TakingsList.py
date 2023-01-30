from time import time

from django.views.generic import ListView
from django.http import Http404

from accounts.mixins import ValidateManagerMixin
from takings.models import Taking


# /taking/list/
class TakingsList(ValidateManagerMixin, ListView):
    template_name = 'takings/list-takings.html'
    model = Taking

    def get(self, request, *args, **kwargs):
        start_time = time()
        self.object_list = self.get_queryset()

        extra_context = {
            'module_name': 'Tomas Físicas',
            'title_page': 'Lista de Tomas',
            'total_records': len(self.object_list),
            'total_time': time() - start_time,
            'last_taking': self.object_list[0],
            'total_groups': 23,
            'total_warenhouses': 12,
        }
        context = self.get_context_data(**kwargs)
        return self.render_to_response({**context, **extra_context})
