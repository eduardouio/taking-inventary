import json
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

from takings.models import Taking

UserModel = get_user_model()


@pytest.mark.django_db
class Test_SyncTakingsDetail:

    @pytest.fixture
    def client(self, client):
        user = UserModel.objects.get(username="sherbas")
        client.force_login(user)
        return client
    
    @pytest.fixture
    def url(slef):
        return reverse("sync-taking-detail")

    def setup_method(self):
        """
        this report for test 
        id_product|boxes|bottles|expiry|year|notes
        3662|12|1|2011-01-21|2011|10 cajas abiertas
        3664|2|2|2022-02-21|2022|5 cajas penidentes
        130|32|3|2022-05-21|2022|
        129|12|4|2011-07-21|2011|
        128|12|3|2010-11-21|2010|
        127|3|2|2011-09-21|2011|
        126|0|1|2012-03-21|2012|3 botellas dañadas
        124|9|2|2013-12-21|2013|
        173|2|3|2014-01-21|2014|
        172|4|4|2015-01-21|2015|
        171|6123|5|2016-01-21|2016|
        169|432|4|2017-03-22|2017|
        168|574|3|2018-03-04|2018|
        165|8|2|2019-03-15|2019|
        159|6|1|2020-03-18|2020|mal arrumado
        158|3|2|2021-01-21|2021|
        156|97|3|2022-01-21|2022|
        155|4|4|2011-01-21|2011|
        154|7|5|2022-01-21|2022|mal ubicado
        152|54|4|2022-01-21|2022|
        151|76|2|2011-01-21|2011|
        150|234|1|2010-01-21|2010|
        146|2324|2|2011-01-21|2011|
        152|54|4|2022-01-21|2022|mal contado primero conteo
        151|76|4|2022-01-21|2022|
        150|234|0|2011-01-21|2011|
        146|2324|0|2010-01-21|2010|
        sumas|12718|71|-|-|-
        """

        key_report = [
            "id_product",
            "taking_total_boxes",
            "taking_total_bottles",
            "date_expiry",
            "year",
            "notes",
        ]

        report = """3662|12|1|2011-01-21|2011|10 cajas abiertas
        3664|2|2|2022-02-21|2022|5 cajas penidentes
        130|32|3|2022-05-21|2022|
        129|12|4|2011-07-21|2011|
        128|12|3|2010-11-21|2010|
        127|3|2|2011-09-21|2011|
        126|0|1|2012-03-21|2012|3 botellas dañadas
        124|9|2|2013-12-21|2013|
        173|2|3|2014-01-21|2014|
        172|4|4|2015-01-21|2015|
        171|6123|5|2016-01-21|2016|
        169|432|4|2017-03-22|2017|
        168|574|3|2018-03-04|2018|
        165|8|2|2019-03-15|2019|
        159|6|1|2020-03-18|2020|mal arrumado
        158|3|2|2021-01-21|2021|
        156|97|3|2022-01-21|2022|
        155|4|4|2011-01-21|2011|
        154|7|5|2022-01-21|2022|mal ubicado
        152|54|4|2022-01-21|2022|
        151|76|2|2011-01-21|2011|
        150|234|1|2010-01-21|2010|
        146|2324|2|2011-01-21|2011|
        152|54|4|2022-01-21|2022|mal contado primero conteo
        151|76|4|2022-01-21|2022|
        150|234|0|2011-01-21|2011|
        146|2324|0|2010-01-21|2010|""".split('\n')
        report = [r.strip().split('|')   for r in report]
        report = [dict(zip(key_report, r)) for r in report]

        for item in report:
            item['id_product'] = int(item['id_product'])
            item['taking_total_boxes'] = int(item['taking_total_boxes'])
            item['taking_total_bottles'] = int(item['taking_total_bottles'])
            item['year'] = int(item['year']) if item['year'] else None

        self.mock_data = {
            "force": False,
            "id_taking": 324,
            "id_team": 1742,
            "token_team": "32b95839deb7d4b6a8d0f74c1a8a342400932c33e12fa8c3ef3fe7f8cd8d88fb",
            "report": report,
        }

        # abrimos la toma para el test
        self.taking = Taking.objects.get(pk=324)
        self.taking.is_active = True
        self.taking.save()
    
    def test_post_success_forced(self, client, url):
        response = client.post(url, self.mock_data)
        assert response.status_code == 201

        self.mock_data['force'] = True
        response_forced = client.post(url, self.mock_data)
        assert response_forced.status_code == 201
        assert response_forced.json() == {'message': "Datos sincronizados de forma Forzada"}

    def test_post_registered_data(self, client, url):
        response = client.post(url, self.mock_data)
        assert response.status_code == 201

        response = client.post(url, self.mock_data)
        assert response.status_code == 400
        assert response.json() == {'message': "Datos ya registrados"}

    
    def test_post_success_data(self, client, url):
        response = client.post(url, self.mock_data)
        assert response.status_code == 201
        response = response.data
        assert response['skus'] == 27
        assert response['quantity'] == 109853
        assert response['taking_total_boxes'] == 12718
        assert response['taking_total_bottles'] == 71
    
    def test_closed_taking(self, client, url):
        self.mock_data['id_taking'] = 303
        response = client.post(url, self.mock_data)
        assert response.status_code == 400
        assert response.data['message'] == "Inventario Cerrado"