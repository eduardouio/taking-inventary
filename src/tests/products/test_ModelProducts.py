import pytest
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist


@pytest.mark.django_db
class TestModelProducts:

    def test_count_products(self):
        products = Product.objects.all()
        assert len(products) > 200

    def test_create_product_with_all_fields(self):
        product = Product.objects.create(
            account_code='12345',
            name='Test Product',
            type_product='ALIMENTO',
            quantity_per_box=10,
            capacity=500,
            unit_measurement='LITROS',
            sale_unit_measurement='UNIDAD',
            alcoholic_strength=40,
            ean_13_code='1234567890123',
            ean_14_code='12345678901234',
            health_register='ABC123',
            image_front=None,
            image_back=None,
            max_stock=100,
            min_stock=10,
            box_dimensions='10x10x10',
            product_dimensions='5x5x5',
            ice_code='ICE123'
        )
        assert product.id_product is not None

        # Tests retrieving a non-existent product by primary key.
    def test_retrieve_nonexistent_product_by_pk(self, mocker):
        mocker.patch.object(
            Product.objects,
            'get',
            side_effect=ObjectDoesNotExist)
        product = Product.get_by_pk(pk=1)
        assert product is None