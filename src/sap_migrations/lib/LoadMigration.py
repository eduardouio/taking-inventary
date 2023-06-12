from common import SAPMigrationConnector
from sap_migrations.models import SapMigration, SapMigrationDetail


class LoadMigration():
    def load(self):
        connector = SAPMigrationConnector()
        current_inventary = connector.runMigration()
        migration = SapMigration.objects.create()
        migration_data = []

        for item in current_inventary:
            migration_detail = SapMigrationDetail(**item)
            migration_detail.id_sap_migration = migration
            migration_data.append(migration_detail)
        SapMigrationDetail.objects.bulk_create(migration_data)

        return migration
