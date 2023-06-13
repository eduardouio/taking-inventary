import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAllSAPMigrationData():
    """Test para el endpoint AllSAPMigrationData"""

    def setup_method(self):
        """Setup para el test"""
        self.client = APIClient()

    def test_load_data(self):
        """Test para el metodo GET"""
        response = self.client.get(reverse('all-sap-migration-data'))
        assert response.status_code == 201
        assert response.json() == {
            'status': 'OK',
            'message': 'AllSAPMigrationData'
        }

    # Tests that no SapMigrationDetail objects are created when current_inventary is empty
    def test_empty_current_inventary(self, mocker):
        mocker.patch(
            'sap_migrations.models.SapMigrationDetail.objects.bulk_create')
        mocker.patch('sap_migrations.models.SapMigration.objects.create')
        mocker.patch('common.SAPMigrationConnector.runMigration',
                     return_value=[])
        migration = LoadMigration().load()
        assert isinstance(migration, SapMigration)
        assert not SapMigrationDetail.objects.filter(
            id_sap_migration=migration).exists()
