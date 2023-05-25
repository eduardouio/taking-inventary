import pytest

from api.Serializers import TeamSerializer
from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserModel


@pytest.mark.django_db
class TestSerializers:
    # Tests creating a new Team object with valid parameters.
    def test_create_team_valid_parameters(self):
        data = {
            'group_number': 1,
            'manager': 2,
            'warenhouse_assistant': 'John Doe',
            'id_taking': 1234,
            'token_team': 'abc123'
        }
        serializer = TeamSerializer(data=data)
        assert serializer.is_valid() is True

    # Tests retrieving a Team object by its primary key.
    def test_retrieve_team_by_pk(self):
        team = Team.objects.create(
            group_number=1,
            manager=CustomUserModel.objects.create(
                username='testuser',
                password='testpassword'
            ),
            warenhouse_assistant='John Doe',
            id_taking=1234,
            token_team='abc123'
        )
        serializer = TeamSerializer(instance=team)
        assert serializer.data['id_team'] == team.id_team

    # Tests creating a new Team object with blank or null fields.
    def test_create_team_blank_null_fields(self):
        data = {
            'group_number': '',
            'manager': None,
            'warenhouse_assistant': '',
            'id_taking': 1234,
            'token_team': ''
        }
        serializer = TeamSerializer(data=data)
        assert serializer.is_valid() is False
