import json

import pytest
from django.contrib.auth import get_user_model as UserModel
from django.urls import reverse
from products.models import Product


@pytest.mark.django_db
class TestTakingAssistantInput:

    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username="evillota")
        client.force_login(user)
        return client

    def setup_method(self):
        self.spected_data = {
            "taking": {
                "id_taking": 191,
                "warenhouses": [
                    "ALMACEN 10 DE AGOSTO",
                    "ALMACÉN GENERAL UIO",
                    "CONSIGNACIONES PB PROVEEDORES"
                ]
            },
            "team": {
                "id_team": 908,
                "manager": 94,
                "id_taking": 191,
            },
            "total_products": 916,
            "spected_products": [
                "VINO CH. TERRA VEGA KOSHER CARMENERE",
                "VINO ARG. SANTA JULIA MERLOT",
                "VINO EU THE PRISONER RED BLEND",
                "VINO ECU. DOS HEMISFERIOS PARADOJA CAB. SAUV. MALBEC",
                "VINO FRA. CHATEAU CANTIN SAINT EMILION GRAND CRU",
                "VINO CH. CARMEN SAUV. BLANC",
                "VINO ESP. EL PULPO ALBARIÑO",
                "VINO ESP. PEÑASOL MERLOT",
                "VINO CH. DONA DOMINGA CHARDONNAY",
                "VINO CH. MONTES SAUV. BLANC CLASSIC SCREW CAP",
                "VINO ESP. TORREMILANOS COLECCION",
            ],
            "user": {
                "username": "evillota",
                "id": 94,
            },
        }

    def test_taking_does_not_exist(self, client):
        url = reverse(
            "api-assistant-input",
            kwargs={'id_taking': 999, 'id_team': 908}
        )
        response = client.get(url)
        assert response.status_code == 404

    def team_does_not_exist(self, client):
        url = reverse(
            "api-assistant-input",
            kwargs={'id_taking': 191, 'id_team': 999}
        )
        response = client.get(url)
        assert response.status_code == 404

    def test_get(self, client):
        url = reverse(
            "api-assistant-input",
            kwargs={'id_taking': 191, 'id_team': 908}
        )
        response = client.get(url)
        assert response.status_code == 200
        response = response.json()
        # comprobamos las bodegas
        assert (
            self.spected_data['taking']['warenhouses']
            ==
            json.loads(response['taking']['warenhouses'])
        )

        # comprobamos la toma
        assert (
            self.spected_data['taking']['id_taking']
            ==
            response['taking']['id_taking']
        )

        # comprobamos el team
        assert (
            self.spected_data['team']['id_team']
            ==
            response['team']['id_team']
        )

        # comprobamos el usuario
        assert (
            self.spected_data['user']['id']
            ==
            response['user']['id']
        )
        assert (
            self.spected_data['user']['username']
            ==
            response['user']['username']
        )
        # comporbamos la cantidad de productos
        assert (
            len(response['products']) ==
            self.spected_data['total_products']
        )

        # comprobamos los productos
        for item in self.spected_data['spected_products']:
            assert item in [x['name'] for x in response['products']]
