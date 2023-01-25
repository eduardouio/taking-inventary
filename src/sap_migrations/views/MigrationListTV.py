from django.views.generic import TemplateView
from sap_migrations.models import SapMigration
from sap_migrations.lib import LoadMigration


# /sap/
class MigrationListTV(TemplateView):
	template_name = 'sap_migrations/list_migrations.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs)

		if request.GET.get('migrate'):
			load_migration = LoadMigration()
			load_migration.load()

		all_migrations = self.get_all_migrations()
		page_data = {
			'all_migrations': all_migrations,
			'module_name': 'Migraciones SAP',
			'title_page': 'Saldos Importados Sap',
			'total_records':len(all_migrations),
		}
		context = { **context, **page_data}
		return self.render_to_response(context=context)

	def get_all_migrations(self):
		all_migrations = [] 
		migrations = SapMigration.objects.all()

		for migration in migrations:
			all_migrations.append({
				'migration': migration,
				'user': SapMigration.get_user(migration)
			})
		return all_migrations
	