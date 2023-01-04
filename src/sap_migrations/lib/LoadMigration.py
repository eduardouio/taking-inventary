from common import SAPMigrationConnector
from sap_migrations.models import SapMigration, SapMigrationDetail


class LoadMigration():
	def load(self):
		connector = SAPMigrationConnector()
		current_inventary = connector.runMigration()
		migration = SapMigration.objects.create()

		for item in current_inventary:
			migration_detail = SapMigrationDetail(**item)
			migration_detail.id_sap_migration = migration
			migration_detail.save()
