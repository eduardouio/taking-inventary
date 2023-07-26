from secrets import token_hex

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from accounts.mixins import ValidateAssistantMixin
from takings.models import Taking


# /taking/<int:id_sap_migration>
# name = mobile-taking
class TakingTV(ValidateAssistantMixin, TemplateView):
    template_name = 'mobile/taking.html'

    def get(self, request, id_taking, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        taking = get_object_or_404(Taking, pk=id_taking)
        user = request.user

        my_team = taking.teams.filter(manager=user).first()
        if not my_team:
            raise Exception('El usuario no es manager de este equipo')

        my_team.token = token_hex(16)
        my_team.save()

        page_data = {
            'title_page': 'Toma Inventario',
            'module_name': 'Toma',
            'id_taking': id_taking,
            'id_team': my_team.pk,
        }

        return self.render_to_response({**context, **page_data})
