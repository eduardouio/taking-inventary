import pytest

from api.Serializers import TakingDetailSerializer


@pytest.mark.django_db
class Test_TakingDetailSerializer:

    def test_create_valid_parameters(self):
        data = {
            "id_taking": 1,
            "account_code": 1,
            "id_team": 1,
            "token_team": "test",
            "taking_total_boxes": 1,
        }

        serializer = TakingDetailSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_blank_null_fields(self):
        data = {
            "id_taking": None,
            "account_code": None,
            "id_team": None,
            "token_team": None,
            "taking_total_boxes": None,
        }

        serializer = TakingDetailSerializer(data=data)
        assert serializer.is_valid() is False
