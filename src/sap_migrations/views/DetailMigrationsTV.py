from django.views.generic import TemplateView
from sap_migrations.models import SapMigrationDetail, SapMigration
from common import loggin


# /sap/detail/<pk>/
class DetailMigrationsTV(TemplateView):
    template_name = 'sap_migrations/detail_migration.html'
    
    def get(self, request, pk, *args, **kwargs):
        loggin('i', 'llamado a detalle de migracion {}'.format(pk))
        context = self.get_context_data(*args, **kwargs)
        page_data = {
            'title_page': 'Detalle De Migracion',
            'migration': self.get_migration_details(pk)
        }
        context = { **context, **page_data }
        return self.render_to_response(context)
    
    def get_migration_details(self, pk):
        pk = int(pk)
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
        
        loggin('i', 'recuperando migracion')
        migration_data['detail'] = SapMigrationDetail.get_by_migration(pk)
        for detail in migration_data['detail']:
            migration_data['warenhouses'].add(detail.warenhouse_name)
            migration_data['products'].add(detail.account_code)
            migration_data['total_items'] += detail.on_hand
        
        migration_data['total_warenhouses'] = len(
            migration_data['warenhouses']
        )
        migration_data['total_products'] = len(
            migration_data['products']
        )
        return migration_data
        
        
        
