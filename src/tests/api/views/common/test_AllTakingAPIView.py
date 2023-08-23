import pytest
from django.contrib.auth import get_user_model as UserModel
from django.urls import reverse


@pytest.mark.django_db
class TestAllTakingData():

    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user)
        return client

    def test_get(self , client):
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
            "manager": {
                "id": 5,
                "username": "lrodriguez",
                "first_name": "LORENA",
                "last_name": "RODRIGUEZ",
                "email": "lorena@vinesa.com.ec",
            }, "all_warenhouses": 40,
            "all_users_assistants": 122,
        }

        url = reverse("all_taking_data", kwargs={"id_taking": 1})
        response = client.get(url)

        # verificams el status code
        assert (response.status_code == 200)
        response = response.json()

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

        # Verificamos manager
        assert (
            spected["manager"]["id"] == response["manager"]["id"]
        )
        assert (
            spected["manager"]["username"] == response["manager"]["username"]
        )
        assert (
            spected["manager"]["first_name"] == response["manager"]["first_name"]
        )
        assert (
            spected["manager"]["last_name"] == response["manager"]["last_name"]
        )
        assert (spected["manager"]["email"] == response["manager"]["email"])

        # comprobamos las boedegas
        assert (spected["all_warenhouses"] == len(response["all_warenhouses"]))

        # verificamos que las bodegas de la toma no esten en la lista
        exclude_warenhouses = [
            'ALMACÉN GENERAL UIO',
            'ALMACEN 10 DE AGOSTO',
            'CONSIGNACIONES PB PROVEEDORES'
        ]

        for item in exclude_warenhouses:
            assert (item not in response["all_warenhouses"])

        # Comprobamos los usuarios con perfil asistentes
        assert (spected["all_users_assistants"] ==
                len(response["all_users_assistants"]))
        
        # comprobamos los reconteos
        assert (len(response["recounts"]) == 4)


    def test_dont_exist_taking(self, client):
        response = client.get("/api/common/taking-data/999/")
        assert (response.status_code == 404)
    
    def test_get_allTakingdata(self, client):
        url = reverse("all_taking_data", kwargs={"id_taking": 170})
        response = client.get(url)
        assert (response.status_code == 200)
        response = response.json()
        assert(len(response["syncs"]["all"]) == 58)

