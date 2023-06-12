import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAllSAPMigrationData():
    """Test para el endpoint AllSAPMigrationData"""

    def setup_method(self):
        """Setup para el test"""
        self.client = APIClient()

    def test_get(self):
        """Test para el metodo GET"""
        response = self.client.get(reverse('all-sap-migration-data'))
        assert response.status_code == 201
        assert response.json() == {
            'status': 'OK',
            'message': 'AllSAPMigrationData'
        }
