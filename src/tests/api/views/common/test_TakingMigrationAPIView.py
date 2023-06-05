# para este test usamos
# migracion 2
# Toma de inventario 1
# prroducto VINO BERONIA CRIANZA 375 ML 01012090550411010375 pk 1306

import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
class TestTakingMigrationAPIView:

    def setup_method(self):
        self.client = APIClient()
        self.account_code = "01012090550411010375"
        self.id_product = 1306
        self.id_taking = 1
        self.id_sap_migracion = 2

    def test_get_success(self):
        spected_data = {
            "migrations": [
                {"warenhouse_name": "ALMACÉN GENERAL UIO", "quantity": 4892},
                {"warenhouse_name": "ALMACÉN GENERAL UIO", "quantity": 155},
                {"warenhouse_name": "ALMACEN 10 DE AGOSTO", "quantity": 108},
            ],
            "takings": [
                {"quantity": 4980},
                {"quantity": 168},
                {"quantity": 7},
            ],
        }

        url = reverse("taking_migration", kwargs={
                      "id_taking": self.id_taking,
                      "account_code": self.account_code}
                      )
        response = self.client.get(url)

        assert response.status_code == 200
        response = response.data
        assert (len(spected_data["takings"]) == len(response["takings"]))
        assert (len(spected_data["migrations"]) == len(response["migrations"]))
        # verificamos la suma de las cantidades de las tomas
        assert (
            sum([x["quantity"] for x in spected_data["takings"]])
            ==
            sum([x["taking"]["quantity"] for x in response["takings"]])
        )

        # verificamos la suma de las cantidades de las migraciones
        assert (
            sum([x["quantity"] for x in spected_data["migrations"]])
            ==
            sum([x["on_hand"] for x in response["migrations"]])
        )

    def test_taking_404(self):
        url = reverse("taking_migration", kwargs={
                      "id_taking": 99999,
                      "account_code": self.account_code}
                      )
        response = self.client.get(url)

        assert response.status_code == 404
        assert response.data["error"] == "Taking not found"

    def tet_product_404(self):
        url = reverse("taking_migration", kwargs={
                      "id_taking": self.id_taking,
                      "account_code": "99999999999999999999"}
                      )
        response = self.client.get(url)

        assert response.status_code == 404
        assert response.data["error"] == "Product not found"
