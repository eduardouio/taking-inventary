from django.views.generic import TemplateView
from sap_migrations.models import SapMigration, SapMigrationDetail
from common import loggin

# /sap/
class MigrationTV(TemplateView):
    template_name = 'sap_migrations/list_migrations.html'
    
    def get(self, request, *args, **kwargs):
        loggin('i', 'llamando a listado de migraciones')
        context = self.get_context_data(*args, **kwargs)
        page_data = {
            'title_page': 'Saldos Importados Sap',
            'all_migrations': self.get_all_migrations()
        }
        context = { **context, **page_data}
        return self.render_to_response(context=context)
    
    def get_all_migrations(self):
        all_migrations = [] 
        migrations = SapMigration.objects.all()

        for migration in migrations:
            detail = SapMigrationDetail.get_by_migration(migration.pk)
            all_migrations.append({
                'migration': migration,
                'detail': detail,
                'user': SapMigration.get_user(migration)
            })
        return all_migrations