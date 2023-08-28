import pytest
from django.contrib.auth import get_user_model as UserModel
from django.urls import reverse
from takings.models import Taking


@pytest.mark.django_db
class TestTakingList:
    """
    Consulta para los dats de prueba
        select * from accounts_customusermodel acc where acc.username  = 'asarmiento'
        select * from takings_taking tt where tt.user_manager_id = 61; 
    """

    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username='asarmiento')
        client.force_login(user)
        return client

    @pytest.fixture
    def client_invalid(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user)
        return client
    
    @pytest.fixture
    def url(self):
        return reverse('takings:taking-list')
    
    def test_list_invalid_user(self, client_invalid, url):
        response = client_invalid.get(url)
        assert response.status_code == 302
    
    def test_list_not_logged(self, client, url):
        client.logout()
        response = client.get(url)
        assert response.status_code == 302
    
    def test_list(self, client, url):
        response = client.get(url)
        assert response.status_code == 200
        report = response.context['object_list']
        assert len(report) == 10

    def test_auditor(self, client, url):
        all_takings = Taking.objects.all()
        user = UserModel().objects.create(
            username='audotoria', role='auditor', password='12345'
        )
        client.force_login(user) 
        response = client.get(url)
        assert response.status_code == 200
        report = response.context['object_list']
        assert len(report) == len(all_takings)