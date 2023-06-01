import pytest

from rest_framework.test import APIClient
from django.urls import reverse

import json
from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserModel
from takings.models import Taking


@pytest.mark.django_db
class TestAddTeamTakingAPIView:

    def setup_method(self):
        self.client = APIClient()

    def test_post(self):
        # recuperamos la toma 1
        taking = Taking.objects.get(pk=1)

        # Usuario grupo neuevo
        manager = CustomUserModel.objects.get(pk=50)

        # recuperamos los grupos de la toma
        first_taking_teams = taking.teams.all()

        # spected_data
        spected_data = [
            {
                'id_taking': 1,
                'group_number': len(first_taking_teams)+1,
                'id': 50,
            }, {
                'id_taking': 1,
                'group_number': len(first_taking_teams)+2,
                'id': 50,
            }, {
                'id_taking': 1,
                'group_number': len(first_taking_teams)+3,
                'id': 50,
            }
        ]

        # mock del nuevo grupo
        mock_post = {
            'teams': [
                {
                    'id_taking': 1,
                    'id': 50,
                },
                {
                    'id_taking': 1,
                    'id': 51,
                },
                {
                    'id_taking': 1,
                    'id': 52,
                },
            ]
        }
        url = reverse('add-team-taking', kwargs={'id_taking': 1})

        # actualizamos lista de teams
        new_taking_teams = taking.teams.all()

        response = self.client.post(
            url,
            data=json.dumps(mock_post),
            content_type='application/json'
        )
        assert response.status_code == 200
        response = response.data
        assert len(response) == len(first_taking_teams) + 3
