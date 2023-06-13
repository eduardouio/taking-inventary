import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAllSAPMigrationData:

    def setuo(self):
        self.client = APIClient()

    def test_get_success_data(self):
        assert (1 == 3)

    def test_not_found_migration(self):
        pass
