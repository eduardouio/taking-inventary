import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from takings.models import TakinDetail


@pytest.mark.django_db
class TestDeleteTakingDetailApiView():

    def setup_method(self):
        self.client = APIClient()

    def test_delete_taking_detail(self):
        # traemos el detalle a eliminar
        item_to_delete = {
            'id_taking_detail': 1357,
        }

        # traemos el detalle a eliminar
        detelet_taking_detail = TakinDetail.objects.get(
            pk=item_to_delete['id_taking_detail']
        )

        assert (detelet_taking_detail is not None)

        # construimos la url
        url = reverse('delete-taking-detail', kwargs={
            'id_taking_detail': item_to_delete['id_taking_detail']
        })

        # hacemos la peticion
        response = self.client.delete(url)

        # verificamos que se elimino
        assert (response.status_code == 204)

        # verificamos que no exista
        detelet_taking_detail = TakinDetail.objects.filter(
            pk=item_to_delete['id_taking_detail']
        )

        assert (len(detelet_taking_detail) == 0)

        def test_delete_taking_detail_not_found(self):
            item_to_delete = {
                'id_taking_detail': 1357000000,
            }

            # construimos la url
            url = reverse('delete-taking-detail', kwargs={
                'id_taking_detail': item_to_delete['id_taking_detail']
            })

            # hacemos la peticion
            response = self.client.delete(url)

            # verificamos que se elimino
            assert (response.status_code == 404)
