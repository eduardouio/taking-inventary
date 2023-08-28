from django.views.generic import TemplateView
from accounts.mixins import ValidateManagerMixin
from takings.models import Taking
from django.http import HttpResponse


# /taking/detail/<int:pk>/
class TakingMasterDetailTV(ValidateManagerMixin, TemplateView):
    template_name = 'takings/taking-detail.html'

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if (self.validate_owner(request, pk)):
            page_data = {
                'id_taking': pk,
                'user': request.user,
            }
            return self.render_to_response(context={**context, **page_data})
        
        return HttpResponse('No tiene permisos para ver esta toma', status=403)

    def validate_owner(self, request, pk):
        """
            Definimos los usuarios con permiso para ver las tomas,
            el owner del registro y el auditor
        """
        if request.user.role == 'auditor':
            return True

        taking = Taking.objects.get(pk=pk)
        if request.user == taking.user_manager:
            return True

        return False