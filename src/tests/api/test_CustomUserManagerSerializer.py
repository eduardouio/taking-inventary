import pytest

from api.Serializers import CustomUserManagerSerializer
from accounts.models.CustomUserModel import CustomUserModel


@pytest.mark.django_db
class Test_CustomUserManagerSerializer:

    def test_create_user_valid_pareters(self):
        data = {
            "username": "test",
            "password": "test",
            "email": "eduardo@sin.com"
        }
        serializer = CustomUserManagerSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_user_blank_null_fields(self):
        data = {
            "username": "",
            "password": "",
            "email": ""
        }
        serializer = CustomUserManagerSerializer(data=data)
        assert serializer.is_valid() is False
