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
        migrations_details = self.get_migration_details(pk)
        page_data = {
            'title_page': 'Detalle De Migracion',
            'migration': migrations_details,
            'module_name': 'Migraciones SAP',
            'total_records': migrations_details['migration']
        }
        context = { **context, **page_data }
        return self.render_to_response(context)
    
    def get_migration_details(self, pk):
        pk = int(pk)
        consolitade_migration = ConsolidateMigration(pk)
        migration_data = {
            'migration': None,
            'detail': [],
            'warenhouses': set(),
            'products': set(),
            'total_warenhouses': 0,
            'total_items':0,
            'total_products':0,
            'total_groups':0,
            'user': None,
        }
        migration_data['migration'] = SapMigration.get(pk)
        migration_data['user'] = SapMigration.get_user(
            migration_data['migration']
        )
        
        if migration_data['migration'] is None:
            loggin('e', 'La migracion {} no existe'.format(pk))
            return migration_data
        
        migration_data['detail'] = consolitade_migration.get_by_product()
        return migration_data