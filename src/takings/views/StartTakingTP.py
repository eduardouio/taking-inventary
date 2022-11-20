from django.views.generic import TemplateView
from sap_migrations.lib import ConsolidateMigration
from warenhouses.models import Warenhouse
from django.core import serializers
import json


# /taking/select/<int:id_sap_migration>/ 
class StartTakingTP(TemplateView):
    template_name = 'takings/start-taking.html'

    def get(self, request, id_sap_migration, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        warenhouses = Warenhouse.objects.all()
        warenhouses_json = serializers.serialize('json', warenhouses)

        page_data = {
            'title_page': 'Custom Taking',
            'module_name': 'Tomas Inventario',
            'pk': id_sap_migration,
            'warenhouses_json': warenhouses_json,
        }

        return self.render_to_response({**context, **page_data})