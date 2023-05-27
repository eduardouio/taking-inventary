import pytest

from api.Serializers import CustomUserSerializer


@pytest.mark.django_db
class Test_CustomUserManagerSerializer:

    def test_create_user_valid_pareters(self):
        data = {
            "username": "test",
            "password": "test",
            "email": "eduardo@sin.com"
        }
        serializer = CustomUserSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_user_blank_null_fields(self):
        data = {
            "username": "",
            "password": "",
            "email": ""
        }
        serializer = CustomUserSerializer(data=data)
        assert serializer.is_valid() is False
