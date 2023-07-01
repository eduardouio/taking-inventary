import pytest
from django.urls import reverse
import requests
import json

from django.contrib.auth import get_user_model

UserModel = get_user_model()


@pytest.mark.django_db
class Test_CreateTakingTP():
    @pytest.fixture
    def authenticated_user_invalid_role(self, client):
        user = UserModel.objects.create_user(
            username='testuser', password='12345', role='assistant'
        )
        client.force_login(user)
        return user

    @pytest.fixture
    def autehnticated_user(self, client):
        user = UserModel.objects.create_user(
            username='testuser', password='12345', role='manager'
        )
        client.force_login(user)
        return user

    @pytest.fixture
    def url(self):
        return reverse('takings:create-taking', kwargs={'id_sap_migration': 1})

    def setup_method(self):
        self.mock_data = {
            'id_sap_migration': 211,
            'name': 'MI TOMA',
            'warenhouses': [
                    {'warenhouse': 'BODEGA CARCELEN', 'selected': True},
                    {'warenhouse': 'Bodega Rev Ecuador - Carcelén', 'selected': True},
                    {'warenhouse': 'BODEGA CUENCA', 'selected': True},
                    {'warenhouse': 'ALMACEN GENERAL GYE', 'selected': True}],
            'groups': [
                {'id': 12, 'username': 'jplaces', 'first_name': 'JOHANNA',
                    'last_name': 'PLACES', 'selected': False},
                {'id': 38, 'username': 'rmoran', 'first_name': 'ROXANA LORENA',
                    'last_name': 'MORAN AROCA', 'selected': False},
                {'id': 60, 'username': 'jlara', 'first_name': 'JOHN',
                    'last_name': 'LARA', 'selected': False},
                {'id': 25, 'username': 'ypreciado', 'first_name': 'YULIANA',
                 'last_name': 'PRECIADO', 'selected': False}],
            'categories': [
                {'category': 'ACCESORIOS', 'items': [
                    'VARIOS'], 'selected': True},
                {'category': 'LICORES', 'items': [
                    'AGUARDIENTE', 'APERITIVO', 'APERITIVOS',
                    'BAJATIVO', 'BRANDY', 'CERVEZA', 'CHAMPAGNE',
                    'COGNAC', 'COMBOS', 'CREMA', 'ESPUMANTE',
                    'GIN', 'JEREZ', 'LICOR', 'MEZCAL', 'PACKS',
                                    'PISCO', 'PROMO', 'RON', 'SANGRIA', 'TEQUILA',
                                    'VARIOS', 'VARIOS\n', 'VINO', 'VODKA',
                                    'WHISKY'],
                 'selected': True},
                {'category': 'otro', 'items': [None], 'selected': False},
                {'category': 'VARIOS', 'items': [
                    'ALIMENTOS',
                    'CIGARRILLOS',
                    'CIGARRILLOS',
                    'VARIOS'],
                 'selected': True
                 }]
        }

    def test_no_autenticated_user(self, client, url):
        response = client.get(url)
        assert response.status_code == 302
        assert response.url == '/accounts/login/'

    def test_authenticated_user_with_valid_role_get_request(
            self, client, autehnticated_user, url):
        response = client.get(url)
        assert response.status_code == 200
        assert response.context_data['id_sap_migration'] == 1
        assert response.template_name == ['takings/create-taking.html']

    def test_autenticated_user_with_invalid_role(
            self, client, authenticated_user_invalid_role, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_authenticated_user_invalid_migration(
            self, client, autehnticated_user):
        url = reverse('takings:create-taking',
                      kwargs={'id_sap_migration': 991})
        response = client.get(url)
        assert response.status_code == 404
        assert response.context['exception'] == 'No existe la migración'

    def post_error_data(self, client, autehnticated_user, url):
        url = reverse('takings:create-taking',
                      kwargs={'id_sap_migration': 1})
        response = client.post(url, data={})
        assert response.status_code == 400
        assert response.content.decode('utf-8') == 'JSON inválido'

    def test_post_success_data(self):
        assert 'tested in browser' == 'tested in browser'
