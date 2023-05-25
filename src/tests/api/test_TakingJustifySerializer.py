import pytest

from api.Serializers import TakingJustifySerializer


@pytest.mark.django_db
class Test_TakingJustifySerializer:

    def test_create_valid_parameters(self):
        data = {
            "id_taking": 1,
            "id_product": 1,
            "justify": "test",
            "audit_comments": "test",
            "is_it_aproved": True,
        }

        serializer = TakingJustifySerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_blank_null_fields(self):
        data = {
            "id_taking": None,
            "id_product": None,
            "justify": None,
            "audit_comments": None,
            "is_it_aproved": None,
        }

        serializer = TakingJustifySerializer(data=data)
        assert serializer.is_valid() is False
