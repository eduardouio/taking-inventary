from django.urls import reverse
import pytest
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@pytest.mark.django_db
class Test_TakingMasterDetail:
    """
    Queries de la tomada de datos
        select * from accounts_customusermodel ac where  ac.id = 5 --lrodrigez gestor
        select * from accounts_customusermodel ac where  ac.id = 12 -- jplaces asistente
        select * from accounts_customusermodel ac where  ac.id = 61 -- asarmiento gestor
        select * from takings_taking tt where tt.id_taking  = 1 
        select tt.id_taking  from takings_taking tt order by tt.created limit 10

    """

    @pytest.fixture
    def client(self, client):
        user = UserModel.objects.get(pk=5)
        client.force_login(user)
        return client
    
    @pytest.fixture
    def client_invalid_role(self, client):
        user = UserModel.objects.get(pk=12)
        client.force_login(user)
        return client
    
    @pytest.fixture
    def client_invalid(self, client):
        user = UserModel.objects.get(pk=61)
        client.force_login(user)
        return client
    
    @pytest.fixture
    def client_auditor(self, client):
        user = UserModel.objects.create(
            username='auditor', role='auditor', password='12345'
        )
        client.force_login(user)
        return client
    
    @pytest.fixture
    def url(self):
        return reverse('takings:master-detail-taking', kwargs={'pk': 1})


    def test_unlogged(self, client, url):
        client.logout()
        response = client.get(url)
        assert response.status_code == 302
    
    def test_invalid_role(self, client_invalid_role, url):
        response = client_invalid_role.get(url)
        assert response.status_code == 302

    def test_ivalid_owner(self, client_invalid, url):
        response = client_invalid.get(url)
        assert response.status_code == 403

    def test_auditor_role(self, client_auditor, url):
        response = client_auditor.get(url)
        assert response.status_code == 200
        takings = [
            1,2,3,4,7,8,9,10,11
        ]
        for tkm in takings:
            url = reverse('takings:master-detail-taking', kwargs={'pk': tkm})
            response = client_auditor.get(url)
            assert response.status_code == 200



