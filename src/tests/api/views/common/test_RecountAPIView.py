import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from takings.lib import ConsolidateTaking
from takings.models import TakinDetail, Taking


@pytest.mark.django_db
class TestRecountAPIView:
    """ Test para el reconteo de un item de una toma
        @item : 01012090550402010750
        @taking : 1
        @url : /api/common/recount/<int:id_taking>/<str:account_code>/
    """

    def setup_method(self):
        # abrimos la toma para correr el test
        takin = Taking.objects.get(pk=1)
        takin.is_active = True
        takin.save()
        self.takin = takin
        self.client = APIClient()

    # testeamos el reconteo de un que se encuentra completo
    # no debe permitir el reconteo
    def test_recount_item_complete_fail_recount(self):
        item_recount = {
            'id_taking': self.takin.pk,
            'account_code': '01012090550402010750',
            'account_code_id': '1406',
            'takings': 6,
        }
        # recuperamos los de talles de la toma
        url = reverse('recount-taking', kwargs={
            'id_taking': item_recount['id_taking'],
            'account_code': item_recount['account_code']}
        )
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {'status': 'ok'}

        # verificamos en la base de datos
        taking_detail = TakinDetail.objects.filter(
            id_taking=item_recount['id_taking']
        ).filter(
            account_code_id=item_recount['account_code_id']
        )

        assert len(taking_detail) == item_recount['takings']

    # testeamos el reconteo de una toma completa
    def test_recount_taking(self):
        url = reverse('recount-taking', kwargs={
            'id_taking': self.takin.pk,
            'account_code': 'all'}
        )

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {'status': 'ok'}

        # comprobamos el reconteo
        incomplete_takings = ConsolidateTaking().get(self.takin.pk)
        # filtramos las incompletas
        incomplete_takings = [
            i for i in incomplete_takings
            if i['is_complete'] is False
        ]

        for item in incomplete_takings:
            assert item['is_complete'] is False
            assert item['taking'] == 0

    def test_taking_closed(self):
        # cerramos la toma
        takin_recount = {
            'id_taking': 3,
            'account_code': '01012090550402010750'
        }

        # para toma
        url = reverse('recount-taking', kwargs={
            'id_taking': takin_recount['id_taking'],
            'account_code': 'all'
        })

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {
            'status': 'No fue posible hacer el reconteo solicitado'
        }

        # para item
        url = reverse('recount-taking', kwargs={
            'id_taking': takin_recount['id_taking'],
            'account_code': takin_recount['account_code']}
        )

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {
            'status': 'No fue posible hacer el reconteo solicitado'
        }

    def test_recount_item(self):
        # comprobamos el reconteo
        incomplete_takings = ConsolidateTaking().get(self.takin.pk)
     
        # filtramos las incompletas
        incomplete_takings = [
            i for i in incomplete_takings
            if i['is_complete'] is False
        ]

        for item in incomplete_takings[:2]:
            # preparamos informacion para el test
            item_recount = {
                'id_taking': self.takin.pk,
                'account_code': item['account_code'],
            }
            url = reverse('recount-taking', kwargs={**item_recount})

            if item['taking'] > 0:
                response = self.client.get(url)
                assert response.status_code == 200
                assert response.data == {'status': 'ok'}

                # verificamos en la base de datos
                taking_detail = TakinDetail.objects.filter(
                    id_taking_id=item_recount['id_taking']
                ).filter(
                    account_code_id=item_recount['account_code']
                )

            assert len(taking_detail) == 0

    def test_recount_item_complete(self):
        # preparamos informacion para el test
        report = ConsolidateTaking().get(1)
        # filtramos las incompletas
        report = [
            i for i in report
            if i['is_complete'] is True
        ]

        for item_recount in report[:2]:
            item = {
                'id_taking': self.takin.pk,
                'account_code': item_recount['account_code'],
            }
            url = reverse('recount-taking', kwargs={**item})
            response = self.client.get(url)
            assert response.status_code == 200
            assert response.data == {'status': 'No fue posible hacer el reconteo solicitado'}