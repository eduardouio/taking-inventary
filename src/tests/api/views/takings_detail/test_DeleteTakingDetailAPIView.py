import pytest
from django.contrib.auth import get_user_model as UserModel
from django.urls import reverse

from takings.models import TakinDetail, Taking


@pytest.mark.django_db
class TestDeleteTakingDetailApiView():

    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user=user)
        return client

    def test_delete_taking_detail(self, client):
        taking = Taking.get(1)
        taking.is_active = True
        taking.save()

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
        response = client.delete(url)

        # verificamos que se elimino
        assert (response.status_code == 204)

        # verificamos que no exista
        detelet_taking_detail = TakinDetail.objects.filter(
            pk=item_to_delete['id_taking_detail']
        )

        assert (len(detelet_taking_detail) == 0)

    def test_delete_taking_detail_not_found(self, client):
        item_to_delete = {
            'id_taking_detail': 1357000000,
        }

        # construimos la url
        url = reverse('delete-taking-detail', kwargs={
            'id_taking_detail': item_to_delete['id_taking_detail']
        })

        # hacemos la peticion
        response = client.delete(url)

        # verificamos que se elimino
        assert (response.status_code == 400)

    def test_delete_taking_close(self, client):
        url = reverse(
            'delete-taking-detail', kwargs={'id_taking_detail': 56921}
        )
        response = client.delete(url)
        assert (response.status_code == 400)