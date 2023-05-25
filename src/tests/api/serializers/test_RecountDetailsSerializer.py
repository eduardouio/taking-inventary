import pytest

from api.Serializers import RecountDetailsSerializer
from recounts.models import RecountDetails


@pytest.mark.django_db
class TestSerializers:
    # Tests that a valid RecountDetails object can be created.
    def test_create_valid_recount_details(self, mocker):
        serializer_data = {
            'id_recount_taking': 1,
            'account_code': 12,
            'taking_total_boxes': 10,
            'taking_total_bottles': 20,
            'quantity': 30,
            'detail': {'key': 'value'}
        }

        # Act
        serializer = RecountDetailsSerializer(data=serializer_data)
        is_valid = serializer.is_valid()

        # Assert
        assert is_valid

    # Tests that a valid RecountDetails object can be serialized.
    def test_serialize_valid_recount_details(self, mocker):
        # Arrange
        serializer_data = {
            'id_recount_taking': 1,
            'account_code': 12,
            'taking_total_boxes': 10,
            'taking_total_bottles': 20,
            'quantity': 30,
            'detail': {'key': 'value'}
        }

        # Act
        serializer = RecountDetailsSerializer(data=serializer_data)
        serializer.is_valid()
        serialized_data = serializer.data
        # Assert
        assert serialized_data['id_recount_taking'] == 1
        assert serialized_data['account_code'] == 12
        assert serialized_data['taking_total_boxes'] == 10
        assert serialized_data['taking_total_bottles'] == 20
        assert serialized_data['quantity'] == 30
        assert serialized_data['detail'] == {'key': 'value'}

    # Tests that a RecountDetails object cannot be created with null fields.
    def test_create_recount_details_with_null_fields(self, mocker):
        # Arrange
        serializer_data = {
            'id_recount_taking': None,
            'account_code': None,
            'taking_total_boxes': None,
            'taking_total_bottles': None,
            'quantity': None,
            'detail': None
        }

        # Act
        serializer = RecountDetailsSerializer(data=serializer_data)
        is_valid = serializer.is_valid()
        assert is_valid is False
