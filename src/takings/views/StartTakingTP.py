from django.views.generic import TemplateView
from sap_migrations.lib import ConsolidateMigration
from warenhouses.models import Warenhouse
from accounts.models import CustomUserModel
import json


# /taking/select/<int:id_sap_migration>/ 
class StartTakingTP(TemplateView):
    template_name = 'takings/start-taking.html'

    def get(self, request, id_sap_migration, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        report_migration = ConsolidateMigration().get(id_sap_migration) 
        all_warenhouses = self.__get_warenhouses_detail(report_migration)
        all_users = CustomUserModel.objects.all()
        all_users = [{
                'username':i.username,
                'first_name': i.first_name,
                'last_name': i.last_name} 
            for i in all_users
         ]
        import ipdb;ipdb.set_trace()

        page_data = {
            'title_page': 'Custom Taking',
            'module_name': 'Tomas Inventario',
            'pk': id_sap_migration,
            'report_migration': report_migration,
            'all_users': all_users,
        }

        return self.render_to_response({**context, **page_data})
    
    def __get_warenhouses_detail(self, report_migration):
        warenhouses = []

        for wrhs in report_migration['by_warenhouses']:
            my_warenhouse = {
                'detail': Warenhouse.get_by_name(wrhs['name']),
                'owners': Warenhouse.get_owners(wrhs['name']),
            }
            warenhouses.append({ ** my_warenhouse ** wrhs['totals']})


