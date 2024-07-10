from time import time

from django.views.generic import TemplateView
from sap_migrations.models import SapMigration
from takings.models import Taking
from django.http import HttpResponseRedirect
from sap_migrations.lib import LoadMigration


# /sap/
class MigrationListTV(TemplateView):
    template_name = 'sap_migrations/list_migrations.html'

    def get(self, request, *args, **kwargs):
        start_time = time()
        message = ''
        context = self.get_context_data(*args, **kwargs)
        action = request.GET.get('action')

        if action == 'migrate':
            load_migration = LoadMigration()
            load_migration.load()
            return HttpResponseRedirect('/sap/?action=migrated')

        if action == 'migrated':
            message = 'Nueva Migracion Completada'

        all_migrations = self.get_all_migrations()

        page_data = {
            'all_migrations': all_migrations,
            'module_name': 'Migraciones SAP',
            'title_page': 'Saldos Importados Sap',
            'total_records': len(all_migrations),
            'last_migration': all_migrations[0] if all_migrations else None,
            'total_time': time() - start_time,
            'message': message,
        }
        context = {**context, **page_data}
        return self.render_to_response(context=context)

    def get_all_migrations(self) -> dict:
        all_migrations = []
        migrations = SapMigration.objects.all()[:5]

        if not migrations:
            return all_migrations

        for migration in migrations:
            all_migrations.append({
                'migration': migration,
                'user': SapMigration.get_user(migration),
                'takings': Taking.get_by_sap_migrations(migration.pk),
            })
        return all_migrations
