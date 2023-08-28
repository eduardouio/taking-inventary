import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model as UserModel
from api.Serializers import CustomUserSerializer
from rest_framework import status


@pytest.mark.django_db
class TestListTakings:

    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user)
        return client

    def setup_method(self):
        user = UserModel().objects.get(username='evillota')

        self.spected_data = {
            'total_takings': 33,
            'sample_takings': [120, 4, 8, 21, 25, 42, 191, 203, 140],
            'user_data': CustomUserSerializer(user).data,
        }

    def test_start(self, client):
        url = reverse('list-taking-mobile', kwargs={'username': 'evillota'})
        response = client.get(url)
        assert response.status_code == 200
        response_data = response.json()
        assert (
            len(response_data['takings']) == self.spected_data['total_takings']
        )
        del (response_data['user_data']['last_login'])
        del (self.spected_data['user_data']['last_login'])
        assert (
            response_data['user_data']
            ==
            self.spected_data['user_data']
        )

        # verificamos la muestra de tomas
        takings = [i['id_taking'] for i in response_data['takings']]
        for tk in self.spected_data['sample_takings']:
            assert tk in takings

    def test_404(self, client):
        url = reverse('list-taking-mobile', kwargs={'username': 'evillota2'})
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_dont_authorize(self, client):
        user = UserModel().objects.get(username='admin')
        client.force_login(user)
        url = reverse('list-taking-mobile', kwargs={'username': 'evillota'})
        response = client.get(url)
        assert response.status_code == status.HTTP_302_FOUND
        assert response.url == '/accounts/logout/'
        
        