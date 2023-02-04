from django.views.generic import TemplateView
from sap_migrations.models import SapMigration
from sap_migrations.lib import ConsolidateMigration
from time import time


# /sap/detail/<pk>/
class DetailMigrationsTV(TemplateView):
    template_name = 'sap_migrations/detail_migration.html'

    def get(self, request, pk, *args, **kwargs):
        start_time = time()
        context = self.get_context_data(*args, **kwargs)
        report_migration = ConsolidateMigration().get(pk)
        conditon_report = 'by_products'

        report = {
            'columns': report_migration['owners'],
            'table': report_migration['table_by_owners']
        }
        # TODO Hacer que se muestre por bodega de forma opcional
        if request.GET.get('criteria') == 'by_owners':
            report = {
                'columns': report_migration['warenhouses'],
                'table': report_migration['table_by_warenhouses']
            }

        page_data = {
            'title_page': 'Detalle De Migracion',
            'report': report,
            'condition_report': conditon_report,
            'module_name': 'Migraciones SAP',
            'total_records': report_migration['totals']['on_hand'],
            'pk': pk,
            'total_time': time() - start_time,
        }
        context = {**context, **page_data}
        return self.render_to_response(context)
