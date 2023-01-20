from django.test import TestCase
from sap_migrations.lib import ConsolidateMigration 
from sap_migrations.models import SapMigration, SapMigrationDetail

class Test_ConsolidateMigrations(TestCase):

    def setUp(self) -> None:
        self.consolidateMigration = ConsolidateMigration()
        return super().setUp()

    def test_get(self):
        report = self.consolidateMigration.get(114)
        
