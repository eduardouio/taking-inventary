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
        url = reverse('api-manager-report', kwargs={'id_taking': 300, 'type_report': 'years'})
        response = client.get(url)
        assert(response.status_code == 200)
        response = response.data
        assert(len(response)  == 406)

    def test_get_report_endData(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 301, 'type_report': 'endDate'})
        response = client.get(url)
        assert(response.status_code == 200)
        response = response.data
        assert(len(response) == 22)
        assert True;

    def test_not_found_taking(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 300000, 'type_report': 'endDate'})
        response = client.get(url)
        assert response.status_code == 400

    def test_not_found_report_name(self, client):
        url = reverse('api-manager-report', kwargs={'id_taking': 300, 'type_report': 'endDateFake'})
        response = client.get(url)
        assert response.status_code == 400