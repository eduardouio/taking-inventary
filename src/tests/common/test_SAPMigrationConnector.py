import pytest
import json
from common import SAPMigrationConnector
from config.secrets_config import SAP_CONNECTION


@pytest.mark.django_db
class TestSAPMigrationConnector:
    """Test para migraciones de SAP"""

    def test_runMigration(self, mocker):
        # mock de respuesta sap
        data = open('tests/mocks/sap_response.json', 'r')
        mock_response = json.loads(data.read())

        migration = SAPMigrationConnector()

        mock_run_migration = mocker.patch.object(
            migration,
            'runMigration',
            return_value=mock_response
        )

        details = migration.runMigration()

        assert (4839 == len(details["response"]))
        mock_run_migration.assert_called_once()

    def test_load_error(self, mocker):
        # corremos el test de errot en la conexion
        SAP_CONNECTION['password'] = 'error'
        migration = SAPMigrationConnector()

        with pytest.raises(Exception):
            migration.runMigration()
