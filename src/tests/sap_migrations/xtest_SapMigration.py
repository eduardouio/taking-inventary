from sap_migrations.models import SapMigration
from tests import TestCaseBase


class Test_SapMigration(TestCaseBase):
    
    def test_get(self):
        sap_migration = SapMigration.get(1)
        no_sap_migration = SapMigration.get(1000)
        self.assertIsInstance(sap_migration, SapMigration)
        self.assertIsNone(no_sap_migration)
    
