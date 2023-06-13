import json

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models.CustomUserModel import CustomUserModel
from sap_migrations.lib import LoadMigration
from sap_migrations.models import SapMigration, SapMigrationDetail


@pytest.mark.django_db
class TestAllSAPMigrationData():
    """Test para el endpoint AllSAPMigrationData"""

    def setup_method(self):
        """Setup para el test"""
        self.client = APIClient()
        self.mock_migration = SapMigration.objects.get(pk=1)
        self.mock_migration_detail = SapMigrationDetail.objects.filter(
            id_sap_migration=self.mock_migration
        )
        self.mock_assistant_users = CustomUserModel.objects.filter(
            role="asistente"
        )

    def test_load_data(self, mocker):
        # spected response
        spected_response = {
            "report": {
                "id_migration": 1,
                "migration_detail": 12824,
                "all_assistant_user": 111,
            }
        }

        # mock sap response
        mocker_migration = mocker.patch.object(
            LoadMigration,
            "load",
            return_value=self.mock_migration
        )
        response = self.client.get(reverse("all-sap-migration-data"))
        assert response.status_code == 200
        response_data = response.json()["report"]
        assert response_data["migration"]["id_sap_migration"] == spected_response["report"]["id_migration"]
        assert len(response_data["migration_detail"]
                   ) == spected_response["report"]["migration_detail"]
        mocker_migration.assert_called_once()
