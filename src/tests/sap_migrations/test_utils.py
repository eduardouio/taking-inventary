from tests import TestCaseBase
from sap_migrations.models import SapMigration, SapMigrationDetail
from sap_migrations.common import get_migration


class Test_common(TestCaseBase):
    
    def test_get_migration(self):
        result = get_migration(1);
        self.assertIsInstance(result['migration'], SapMigration)
        self.assertIsInstance(result['detail'], list)
        
        fake_migration = get_migration(999999)
        self.assertEqual(fake_migration['migration'], None) 
        self.assertEqual(fake_migration['detail'], []) 