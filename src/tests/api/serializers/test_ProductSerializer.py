import pytest

from api.Serializers import ProductSerializer
from products.models import Product


@pytest.mark.django_db
class TestSerializers:
    def test_create_product_with_all_required_fields(self, mocker):
        mock_serializer_data = {
            'account_code': '1234',
            'name': 'Test Product',
            'type_product': 'ACCESORIO',
            'quantity_per_box': 1,
            'capacity': 10,
            'unit_measurement': 'MILITROS',
            'sale_unit_measurement': 'test',
        }
        mock_serializer = ProductSerializer(data=mock_serializer_data)
        result = mock_serializer.is_valid()

        # Assert
        assert result is True

    def test_update_product_with_valid_data(self, mocker):
        # Arrange
        mock_product = Product(
            account_code='1234',
            name='Test Product',
            type_product='ACCESORIO',
            quantity_per_box=1,
            capacity=10,
            unit_measurement='test',
            sale_unit_measurement='test',
        )
        mock_serializer_data = {
            'account_code': '1234',
            'name': 'Updated Test Product',
            'type_product': 'ALIMENTO',
            'quantity_per_box': 2,
            'capacity': 20,
            'unit_measurement': 'LITROS',
            'sale_unit_measurement': 'updated_test',
        }
        mock_serializer = ProductSerializer(
            instance=mock_product, data=mock_serializer_data)

        result = mock_serializer.is_valid()

        # Assert
        assert result is True

    def test_create_product_with_empty_or_invalid_fields(self, mocker):
        # Arrange
        mock_serializer_data = {
            'account_code': '',
            'name': '',
            'type_product': 'invalid',
            'quantity_per_box': -1,
            'capacity': -10,
            'unit_measurement': 'invalid',
            'sale_unit_measurement': 'invalid',
        }
        mock_serializer = ProductSerializer(data=mock_serializer_data)

        # Act
        result = mock_serializer.is_valid()

        # Assert
        assert result is False

    def test_update_product_with_invalid_data(self, mocker):
        # Arrange
        mock_product = Product(
            account_code='1234',
            name='Test Product',
            type_product='test',
            quantity_per_box=1,
            capacity=10,
            unit_measurement='test',
            sale_unit_measurement='test',
        )
        mock_serializer_data = {
            'account_code': '',
            'name': '',
            'type_product': 'invalid',
            'quantity_per_box': -1,
            'capacity': -10,
            'unit_measurement': 'invalid',
            'sale_unit_measurement': 'invalid',
        }
        mock_serializer = ProductSerializer(
            instance=mock_product, data=mock_serializer_data)

        # Act
        result = mock_serializer.is_valid()

        # Assert
        assert result is False
