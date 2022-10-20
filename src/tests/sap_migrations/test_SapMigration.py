from sap_migrations.models import SapMigration
from django.test import TestCase
from faker import Faker


class Test_SapMigration(TestCase):

    def setUp(self):
        for item in range(10):
            sap_migration = SapMigration.objects.create()
    
    def test_get(self):
        sap_migration = SapMigration.get(1)
        no_sap_migration = SapMigration.get(1000)
        self.assertIsInstance(sap_migration, SapMigration)
        self.assertIsNone(no_sap_migration)
          