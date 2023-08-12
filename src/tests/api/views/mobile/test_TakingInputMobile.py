import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model as UserModel


@pytest.mark.django_db
class TestTakingInputMobile:

    @pytest.fixture
    def client(self, client):
        user = UserModel().get(username='test')
        client.force_login(user)
        return client