import pytest
from sap_migrations.lib import LoadMigration
from sap_migrations.models import SapMigration
from common import SAPMigrationConnector
import json


@pytest.mark.django_db
class TestLoadMigration:

    def setup_method(self):
        self.load_migration = LoadMigration()

    def test_load(self, mocker):
        # mock sap response
        data = open('tests/mocks/sap_response.json', 'r')
        mock_response = json.loads(data.read())

        mocker_migration = mocker.patch.object(
            SAPMigrationConnector,
            'runMigration',
            return_value=mock_response['response']
        )

        migration = self.load_migration.load()

        assert isinstance(migration, SapMigration)
        mocker_migration.assert_called_once()
