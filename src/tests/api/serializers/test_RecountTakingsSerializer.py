import pytest

from api.Serializers import RecountTakingsSerializer
from recounts.models import RecountTakings


@pytest.mark.django_db
class TestSerializer:

    def test_create_valid_parameters(self):
        data = {
            "id_taking": 1,
        }

        serializer = RecountTakingsSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_blank_null_fields(self):
        data = {
            "id_taking": None,
        }

        serializer = RecountTakingsSerializer(data=data)
        assert serializer.is_valid() is False
