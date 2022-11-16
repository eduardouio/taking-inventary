from django.views.generic import TemplateView
from sap_migrations.models import SapMigration
from sap_migrations.lib import ConsolidateMigration
from common import loggin


# /sap/detail/<pk>/
class DetailMigrationsTV(TemplateView):
    template_name = 'sap_migrations/detail_migration.html'
    
    def get(self, request, pk, *args, **kwargs):
        loggin('i', 'llamado a detalle de migracion {}'.format(pk))
        context = self.get_context_data(*args, **kwargs)
        report_migrarion = ConsolidateMigration().get(pk)
        conditon_report = 'by_products'

        if request.GET:
            conditon_report = request.GET.get('criteria')

        page_data = {
            'title_page': 'Detalle De Migracion',
            'report': report_migrarion,
            'condition_report': conditon_report,
            'module_name': 'Migraciones SAP',
            'total_records': report_migrarion['totals']['on_hand']
        }
        context = { **context, **page_data }
        return self.render_to_response(context)