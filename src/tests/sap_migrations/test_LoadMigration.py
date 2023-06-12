import pytest
import json
from sap_migrations.lib import LoadMigration
from common import SAPMigrationConnector
from sap_migrations.models import SapMigration, SapMigrationDetail


@pytest.mark.django_db
class TestLoadMigration:
    """Test para migraciones de SAP"""

    def setup_method(self):
        self.load_migration = LoadMigration()

    def test_load_sucess(self, mocker):
        # mock de respuesta sap
        data = open('tests/mocks/sap_response.json', 'r')
        mock_response = json.loads(data.read())
        migration = SAPMigrationConnector()
        mocker.patch.object(
            migration,
            'runMigration',
            return_value=mock_response
        )
        details = migration.runMigration()
        assert (1030 == len(details["response"]))

    def test_load_error(self, mocker):
        pass
