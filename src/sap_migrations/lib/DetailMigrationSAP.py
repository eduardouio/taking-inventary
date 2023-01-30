from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import Taking


class DetailMigrationSAP():

    def get(self, id_sap_migration):
        report = {
            'user': None,
            'takings': None,
        }

        sap_migration = SapMigration.get(id_sap_migration)
        if not sap_migration:
            return report
       
        report['user'] = sap_migration.get_user()
        report['takings'] = Taking.get_by_sap_migrations(id_sap_migration)
        return report