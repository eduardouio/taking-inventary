from time import time
import json

from django.views.generic import ListView
from django.http import Http404

from accounts.mixins import ValidateManagerMixin
from takings.models import Taking, TakinDetail


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
        }
        context = self.get_context_data(**kwargs)
        return self.render_to_response({**context, **extra_context})

    def get_queryset(self):
        queryset = Taking.objects.all()
        for item in queryset:
            item.takings_details = TakinDetail.get_by_taking(item.id_taking)
            if item.warenhouses:
                item.warenhouses = json.loads(item.warenhouses)
            else:
                item.warenhouses = []

        return queryset
