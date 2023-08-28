import pytest
from django.contrib.auth import get_user_model as UserModel
from django.urls import reverse


@pytest.mark.django_db
class Test_ReportManagerApiView():

    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user)
        return client
    
    def test_get_report_years(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 300})
        response = client.get(url)
        assert(response.status_code == 200)
        response = response.data
        response = [r for r in response if r['year']]
        assert(len(response)  == 406)

    def test_get_report_endData(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 301})
        response = client.get(url)
        assert(response.status_code == 200)
        response = response.data
        response = [r for r in response if r['date_expiry']]
        assert(len(response) == 22)

    def test_get_all_report(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 301})
        response = client.get(url)
        assert(response.status_code == 200)
        response = response.data
        assert(len(response) == 1134)

    def test_get_news_report(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 301})
        response = client.get(url)
        assert(response.status_code == 200)
        response = response.data
        response = [r for r in response if r['notes']]
        assert(len(response) == 61)

    def test_not_found_taking(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 300000})
        response = client.get(url)
        assert response.status_code == 400
