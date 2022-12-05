from django.views.generic import TemplateView
from sap_migrations.lib import ConsolidateMigration
from warenhouses.models import Warenhouse
from accounts.models import CustomUserModel
from django.core.serializers import serialize
import json


# /taking/select/<int:id_sap_migration>/ 
class CreateTakingTP(TemplateView):
    template_name = 'takings/start-taking.html'

    def get(self, request, id_sap_migration, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        report_migration = ConsolidateMigration().get(id_sap_migration) 
        all_warenhouses = self.__get_warenhouses_detail(report_migration)
        all_users = CustomUserModel.objects.all()
        all_users = [{
                'username':i.username,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'role': i.role,
                'is_selected': False} 
            for i in all_users if i.role == 'asistente'
         ]
        page_data = {
            'title_page': 'Custom Taking',
            'module_name': 'Tomas Inventario',
            'pk': id_sap_migration,
            'report_migration': report_migration,
            'all_users': json.dumps(all_users),
            'all_warenhouses': json.dumps(all_warenhouses),
        }
        return self.render_to_response({**context, **page_data})
    
    def post(self, request, *args, **kwargs):
        import ipdb;ipdb.set_trace()

    def __get_warenhouses_detail(self, report_migration):
        warenhouses = []
        for wrhs in report_migration['by_warenhouses']:
            my_warenhouse = {
                'detail': json.loads(serialize(
                    'json', 
                    [Warenhouse.get_by_name(wrhs['name'])])
                )[0],
                'owners': Warenhouse.get_owners(wrhs['name']),
                'is_selected': False,
            }
            warenhouses.append({ ** my_warenhouse, ** wrhs['totals']})

        return warenhouses


