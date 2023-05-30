import pytest
import json

from rest_framework.test import APIClient
from django.urls import reverse

from takings.models import Taking


@pytest.mark.django_db
class TestUpdateTakingView:
    def setup_method(self):
        self.client = APIClient()

    def test_put_valid_data(self):
        updated_taking = {
            "id_taking": 1,
            "created": "2023-03-04T06:11:06.571206",
            "modified": "2023-05-27T04:11:06.269441",
            "is_active": False,
            "id_user_created": 5,
            "id_user_updated": 2,
            "notes": "BODEGA GENERAL 10 DE AGOSTO, NOTAS ADICIONALES",
            "hour_start": "06:11:06",
            "hour_end": None,
            "warenhouses": ["ALMACÉN GENERAL UIO", "ALMACEN 10 DE AGOSTO", "CONSIGNACIONES PB PROVEEDORES", "LAGUARDA CUENCA"],
            "name": "BODEGA GENERAL 10 DE AGOSTO",
            "location": "SERVMULTIMARC",
            "total_warenhouses": 4,
            "total_products_unities": 0,
            "total_groups": 15,
            "total_products": 0,
            "have_report": False,
            "audit_comments": None,
            "is_it_audited": False,
            "id_sap_migration": 2,
            "user_manager": 5,
            "teams": [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        }
        # moock taking
        taking = Taking.objects.get(pk=1)
        # construct url
        url = reverse('update_taking', kwargs={'id_taking': taking.id_taking})
        # moock request
        response = self.client.put(
            url,
            json.dumps(updated_taking),
            content_type='application/json'
        )
        # moock view
        assert (response.status_code == 200)
        response = response.data

        assert (response["id_taking"] == updated_taking["id_taking"])
        assert (response["notes"] == updated_taking["notes"])
        assert (response["warenhouses"] == updated_taking["warenhouses"])
        assert (response["location"] == updated_taking["location"])
        assert (response["teams"] == updated_taking["teams"])

    def test_put_invalid_data(self):
        updated_taking = {
            "id_taking": 1,
            "is_active": False,
            "id_user_created": 5,
            "id_user_updated": 2,
            "notes": "BODEGA GENERAL 10 DE AGOSTO, NOTAS ADICIONALES",
            "hour_start": "06:11:06",
            "hour_end": None,
            "warenhouses": ["ALMACÉN GENERAL UIO", "ALMACEN 10 DE AGOSTO", "CONSIGNACIONES PB PROVEEDORES", "LAGUARDA CUENCA"],
            "name": "BODEGA GENERAL 10 DE AGOSTO",
            "location": "INVALID",
            "user_manager": 5,
        }

        # moock taking
        taking = Taking.objects.get(pk=1)
        # construct url
        url = reverse('update_taking', kwargs={'id_taking': taking.id_taking})
        # moock request
        response = self.client.put(
            url,
            json.dumps(updated_taking),
            content_type='application/json'
        )
        # moock view
        assert (response.status_code == 400)
        errors_spected = ['location', 'id_sap_migration', 'teams']
        errors = [i for i in response.json().keys()]
        assert (errors_spected == errors)

    def test_does_not_exist(self):
        updated_taking = {
            "id_taking": 1,
            "is_active": False,
            "id_user_created": 5,
            "id_user_updated": 2,
            "notes": "BODEGA GENERAL 10 DE AGOSTO, NOTAS ADICIONALES",
            "hour_start": "06:11:06",
            "hour_end": None,
            "warenhouses": ["ALMACÉN GENERAL UIO", "ALMACEN 10 DE AGOSTO", "CONSIGNACIONES PB PROVEEDORES", "LAGUARDA CUENCA"],
            "name": "BODEGA GENERAL 10 DE AGOSTO",
            "location": "INVALID",
            "user_manager": 5,
        }

        # moock taking
        # construct url
        url = reverse('update_taking', kwargs={'id_taking': 9797})
        # moock request
        response = self.client.put(
            url,
            json.dumps(updated_taking),
            content_type='application/json'
        )
        # moock view
        assert (response.status_code == 404)

    def test_one_field_update(self):
        taking = Taking.objects.get(pk=1)

        updated_taking = {
            "id_taking": 1,
            "warenhouses": ["ALMACÉN GENERAL UIO"],
            "id_sap_migration": 2,
            "user_manager": 5,
            "teams": [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        }

        url = reverse('update_taking', kwargs={'id_taking': taking.id_taking})
        # moock request
        response = self.client.put(
            url,
            json.dumps(updated_taking),
            content_type='application/json'
        )
        # moock view
        assert (response.status_code == 200)
        response = response.data

        assert (response["warenhouses"] == updated_taking["warenhouses"])
