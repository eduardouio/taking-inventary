import pytest

from api.Serializers import SapMigrationDetailSerializer


@pytest.mark.django_db
class Test_SapMigrationDetailSerializer:

    def test_create_success(self):
        mock_serializer_data = {
            "id_sap_migration": 1,
            "company_name": "Test Company'",
            "account_code": "1234'",
            "ean_13_code": "5678'",
            "health_register": "Test Product'",
            "name": "Test Product'",
            "id_warenhouse_sap_code": "ABC'",
            "warenhouse_name": "Test Warehouse'",
            "quantity_per_box": "10",
            "on_hand": "20",
            "on_order": "5",
            "is_commited": "3",
            "avaliable": "12",
        }

        mock_serializer = SapMigrationDetailSerializer(
            data=mock_serializer_data
        )

        assert mock_serializer.is_valid() is True

    def test_create_error(self):
        mock_serializer_data = {}

        mock_serializer = SapMigrationDetailSerializer(
            data=mock_serializer_data
        )
        assert mock_serializer.is_valid() is False
