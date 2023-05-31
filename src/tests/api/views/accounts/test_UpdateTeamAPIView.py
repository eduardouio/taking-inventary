import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from api.views.accounts import UpdateTeamAPIView


@pytest.mark.django_db
class TestUpdateTeamAPIView(APIClient):

    def test_update_team(self):
        url = reverse('update-team', kwargs={'id_team': 1})
        response = self.put(url, data={'name': 'test'})
        assert response.status_code == 200
        assert response.data['name'] == 'test'
