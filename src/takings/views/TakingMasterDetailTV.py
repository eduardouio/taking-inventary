from time import time

from django.views.generic import TemplateView

from accounts.mixins import ValidateManagerMixin


# /taking/detail/<int:pk>/
class TakingMasterDetailTV(ValidateManagerMixin, TemplateView):
    template_name = 'takings/taking-detail.html'

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        page_data = {
            'id_taking': pk,
            'user': request.user,
        }
        return self.render_to_response(context={**context, **page_data})
