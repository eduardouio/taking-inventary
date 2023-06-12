from tests import TestCaseBase
from sap_migrations.models import SapMigrationDetail


class Test_SapMigrationDetail(TestCaseBase):
    
    def test(self):
        migration_detail = SapMigrationDetail.get(1)
        self.assertIsInstance(migration_detail, SapMigrationDetail)
        
        fake_migration_detail = SapMigrationDetail.get(-1)
        self.assertIsNone(fake_migration_detail)