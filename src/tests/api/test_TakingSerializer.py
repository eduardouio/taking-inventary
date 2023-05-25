import pytest

from api.Serializers import TakingSerializer


@pytest.mark.django_db
class Test_TakingSerializet:

    def test_create_valid_parameters(self):
        data = {
            "id_sap_migration": 1,
            "user_manager": 1,
            "teams": [1, 2, 3],
            "name": "test",
        }

        serializer = TakingSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_blank_null_fields(self):
        data = {
            "id_sap_migration": None,
            "user_manager": 1,
            "teams": [1, 2, 3],
            "name": "test",
        }

        serializer = TakingSerializer(data=data)
        assert serializer.is_valid() is False
