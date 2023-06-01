import pytest
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.test import APIClient

from api.views.accounts import CreateTeamAPIView
from accounts.models.Team import Team


@pytest.mark.django_db
class TestCreateTeamAPIView():
    # Tests that valid data is posted and a new team is created successfully.
    def test_valid_data_creates_new_team(self, mocker):
        """
        Test that valid data is posted and a new team is created successfully.
        """
        team_data = {
            "group_number": 1,
            "manager": 1,
            "warenhouse_assistant": "John Doe",
            "id_taking": 1,
            "token_team": "abc123"
        }
        serializer_mock = mocker.Mock()
        serializer_mock.is_valid.return_value = True
        serializer_mock.data = team_data
        create_mock = mocker.patch.object(CreateTeamAPIView, 'perform_create')
        create_mock.return_value = None
        response_mock = mocker.Mock()
        response_mock.data = team_data
        mocker.patch.object(Response, '__new__', return_value=response_mock)

        request_mock = mocker.Mock()
        request_mock.data = team_data

        view = CreateTeamAPIView()
        view.post(request_mock)

        serializer_mock.is_valid.assert_called_once_with()
        create_mock.assert_called_once_with(serializer_mock)
        Response.__new__.assert_called_once_with(Response, team_data)

    # Tests that invalid data is posted and appropriate error response is returned.
    def test_invalid_data_returns_appropriate_error(self, mocker):
        """
        Test that invalid data is posted and appropriate error response is returned.
        """
        team_data = {
            "group_number": "invalid",
            "manager": 1,
            "warenhouse_assistant": "John Doe",
            "id_taking": 1,
            "token_team": "abc123"
        }
        serializer_mock = mocker.Mock()
        serializer_mock.is_valid.return_value = False
        serializer_mock.errors = {'group_number': ['Invalid value']}
        response_mock = mocker.Mock()
        response_mock.status_code = 400
        response_mock.data = {'group_number': ['Invalid value']}
        mocker.patch.object(Response, '__new__', return_value=response_mock)

        request_mock = mocker.Mock()
        request_mock.data = team_data

        view = CreateTeamAPIView()
        response = view.post(request_mock)

        serializer_mock.is_valid.assert_called_once_with()
        Response.__new__.assert_called_once_with(
            Response, {'group_number': ['Invalid value']})
        assert response.status_code == 400

    # Tests the behavior when the serializer is not valid.
    def test_when_serializer_is_not_valid(self, mocker):
        """
        Test the behavior when the serializer is not valid.
        """
        team_data = {
            "group_number": "invalid",
            "manager": 1,
            "warenhouse_assistant": "John Doe",
            "id_taking": 1,
            "token_team": "abc123"
        }
        serializer_mock = mocker.Mock()
        serializer_mock.is_valid.return_value = False
        serializer_mock.errors = {'group_number': ['Invalid value']}
        mocker.patch.object(CreateTeamAPIView, 'get_serializer',
                            return_value=serializer_mock)

        request_mock = mocker.Mock()
        request_mock.data = team_data

        view = CreateTeamAPIView()
        response = view.post(request_mock)

        serializer_mock.is_valid.assert_called_once_with()
        assert response.status_code == 400

    # Tests that the serializer is validated before creating a new team.
    def test_serializer_is_validated_before_creating_team(self, mocker):
        """
        Test that the serializer is validated before creating a new team.
        """
        team_data = {
            "group_number": 1,
            "manager": 1,
            "warenhouse_assistant": "John Doe",
            "id_taking": 1,
            "token_team": "abc123"
        }
        serializer_mock = mocker.Mock()
        serializer_mock.is_valid.return_value = True
        mocker.patch.object(CreateTeamAPIView, 'get_serializer',
                            return_value=serializer_mock)

        request_mock = mocker.Mock()
        request_mock.data = team_data

        view = CreateTeamAPIView()
        view.post(request_mock)

        serializer_mock.is_valid.assert_called_once_with()

    # Tests that the created team data is returned in the response.
    def test_created_team_data_is_returned_in_response(self, mocker):
        """
        Test that the created team data is returned in the response.
        """
        team_data = {
            "group_number": 1,
            "manager": 1,
            "warenhouse_assistant": "John Doe",
            "id_taking": 1,
            "token_team": "abc123"
        }
        serializer_mock = mocker.Mock()
        serializer_mock.is_valid.return_value = True
        serializer_mock.data = team_data
        create_mock = mocker.patch.object(CreateTeamAPIView, 'perform_create')
        create_mock.return_value = None
        response_mock = mocker.Mock()
        response_mock.data = team_data
        mocker.patch.object(Response, '__new__', return_value=response_mock)

        request_mock = mocker.Mock()
        request_mock.data = team_data

        view = CreateTeamAPIView()
        response = view.post(request_mock)

        Response.__new__.assert_called_once_with(Response, team_data)
        assert response.data == team_data

    # Tests the behavior when the team creation fails.
    def test_when_team_creation_fails(self, mocker):
        """
        Test the behavior when the team creation fails.
        """
        team_data = {
            "group_number": 1,
            "manager": 1,
            "warenhouse_assistant": "John Doe",
            "id_taking": 1,
            "token_team": "abc123"
        }
        serializer_mock = mocker.Mock()
        serializer_mock.is_valid.return_value = True
        create_mock = mocker.patch.object(CreateTeamAPIView, 'perform_create')
        create_mock.side_effect = Exception('Error creating team')
        response_mock = mocker.Mock()
        response_mock.status_code = 500
        response_mock.data = {'error': 'Error creating team'}
        mocker.patch.object(Response, '__new__', return_value=response_mock)

        request_mock = mocker.Mock()
        request_mock.data = team_data

        view = CreateTeamAPIView()
        response = view.post(request_mock)

        serializer_mock.is_valid.assert_called_once_with()
        create_mock.assert_called_once_with(serializer_mock)
        Response.__new__.assert_called_once_with(
            Response, {'error': 'Error creating team'})
        assert response.status_code == 500
