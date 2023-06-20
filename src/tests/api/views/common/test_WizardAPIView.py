import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestWizardAPIView:

    def setup_method(self):
        self.client = APIClient()
        self.client.login(username='admin', password='1234.abc')

    def test_get_success_data(self):
        url = reverse('wizard-assistant', kwargs={'id_sap_migration': 1})
        response = self.client.get(url)
        assert response.status_code == 200

    def test_not_found_data(self):
        url = reverse('wizard-assistant', kwargs={'id_sap_migration': 1000})
        spected_reponse = {
            "detail": "No existe la migración de SAP con id: 1000"}
        response = self.client.get(url)
        assert response.status_code == 404
        assert response.json() == spected_reponse
