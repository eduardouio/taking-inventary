from time import time
import json

from django.views.generic import ListView

from accounts.mixins import ValidateManagerMixin
from takings.models import Taking, TakinDetail


# /taking/list/
class TakingsList(ValidateManagerMixin, ListView):
    template_name = 'takings/list-takings.html'
    model = Taking

    def get(self, request, *args, **kwargs):
        start_time = time()
        message = ''

        if request.GET.get('action') == 'delete':
            my_taking = Taking.get(request.GET.get('pk'))
            if my_taking:
                my_taking_details = TakinDetail.get_by_taking(
                    request.GET.get('pk')
                )
                if not my_taking_details:
                    message = 'Toma {} eliminada correctamente'.format(
                        request.GET.get('pk')
                    )
                    try:
                        my_taking.delete()
                    except:
                        message = 'No se puede Eliminar el registro, tiene dependencias, si desea eliminar comunicarse con soporte@vinesa.com.ec'

        self.object_list = self.get_queryset()
        extra_context = {
            'module_name': 'Tomas Físicas',
            'title_page': 'Lista de Tomas',
            'total_records': len(self.object_list),
            'total_time': time() - start_time,
            'last_taking': self.object_list[0],
            'message': message,
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
