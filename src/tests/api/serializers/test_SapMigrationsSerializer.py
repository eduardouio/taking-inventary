import pytest

from api.Serializers import SapMigrationSerializer


@pytest.mark.django_db
class Test_SapMigration:

    def test_create_migration_success(self, mocker):
        mock_serializer_data = {
            "total_warenhouses": "10",
            "total_products_unities": "100",
            "total_groups": "5",
            "total_products": "500",
            "have_report": "True",
            "have_taking": "False",
            "report": "{'key': 'value'}",
            "products": "{'key': 'value'}",
            "warenhouses": "{'key': 'value'}",
            "owners": "{'key': 'value'}"
        }

        mock_serializer = SapMigrationSerializer(data=mock_serializer_data)
        assert mock_serializer.is_valid() == True

    def test_create_migration_incomplete(self, mocker):
        mock_serializer_data = {
            "total_warenhouses": "error",
            "total_products_unities": "100",
            "total_groups": "errorr",
            "total_products": "500",
            "have_report": "True",
            "have_taking": "False",
            "report": "{'key': 'value'}",
            "products": "{'key': 'value'}",
            "warenhouses": "{'key': 'value'}",
            "owners": "{'key': 'value'}"
        }

        mock_serializer = SapMigrationSerializer(data=mock_serializer_data)
        assert mock_serializer.is_valid() == False
