from tests import TestCaseBase
from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import Taking, TakinDetail
from sap_migrations.common import get_migration, get_taking


class Test_common(TestCaseBase):
    
    def test_get_migration(self):
        result = get_migration(1);
        self.assertIsInstance(result['migration'], SapMigration)
        self.assertIsInstance(result['detail'], list)
        
        fake_migration = get_migration(999999)
        self.assertEqual(fake_migration['migration'], None) 
        self.assertEqual(fake_migration['detail'], []) 
    
    def test_get_taking(self):
        result = get_taking(1)
        self.assertIsInstance(result['taking'], Taking)
        self.assertIsInstance(result['detail'], list)
        
        fake_taking = get_taking(99999)
        self.assertEqual(fake_taking['taking'], None)        
        self.assertEqual(fake_taking['detail'], [])
