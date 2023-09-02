import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models.Team import Team


@pytest.mark.django_db
class TestUpdateTeamAPIView():

    def setup_method(self):
        self.client = APIClient()
        # recuperamso equipo original
        self.team_data = Team.objects.get(pk=1)

    def test_update_team_success(self):

        # datos a modificar
        my_updated_team = {
            'id_team': 1,
            'id_taking': 1,
            'manager': self.team_data.manager.id,
            'notes': 'Camabiamos el nombre del equipo',
            'warenhouse_assistant': 'Nuevo Nombre Asistente',
        }

        url = reverse('update-team', kwargs={'id_team': 1})
        response = self.client.put(url, data=my_updated_team)
        assert response.status_code == 200

        # verificamos los cambios
        updated_data = Team.objects.get(pk=1)
        assert updated_data.notes == my_updated_team['notes']
        assert updated_data.warenhouse_assistant == my_updated_team['warenhouse_assistant']
