import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAllTakingData():

    def setup_method(self):
        self.client = APIClient()

    def test_get(self):
        """Test for get method, with spected data"""
        spected = {
            "id_taking": 1,
            "lenght_report": 868,
            "total_bottles": 733912,
            "total_bottles_sap": 739853,
            "total_groups": 20,
            "enterprises": [
                "VIDINTERNACIONAL S.A.",
                "REV ECUADOR S.A",
                "CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.",
                "AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.",
                "VINOS Y ESPIRITUOSOS VINESA S.A",
                "IMNAC IMPORTADORA NACIONAL CIA LTDA",
            ],
        }

        response = self.client.get("/api/all-taking-data/1/")

        # verificams el status code
        assert (response.status_code == 200)

        response = response.data

        # comporbamos el id toma
        assert (
            spected["id_taking"] == response["taking"]["id_taking"]
        )

        # verificamos items de toma
        assert (len(response["report"]) == spected["lenght_report"])

        # vericiamos items totale en botellas
        total_bottles = sum([i["tk_quantity"] for i in response["report"]])
        total_bottles_sap = sum([i["sap_stock"] for i in response["report"]])

        assert (total_bottles == spected["total_bottles"])
        assert (total_bottles_sap == spected["total_bottles_sap"])

        # verificamos empresas
        assert (len(spected["enterprises"]) == len(response["enterprises"]))
        for item in spected["enterprises"]:
            assert (item in response["enterprises"])

        # verificamos grupos
        assert (len(response["teams"]) == spected["total_groups"])
        0/0

    def test_dont_exist_taking(self):
        response = self.client.get("/api/all-taking-data/999/")
        assert (response.status_code == 404)
