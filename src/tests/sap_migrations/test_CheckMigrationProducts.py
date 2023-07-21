import pytest

from products.models import Product
from sap_migrations.lib import CheckMigrationProducts
from sap_migrations.models import SapMigrationDetail, SapMigration


@pytest.mark.django_db
class TestCheckMigrationProducts:

    @pytest.fixture
    def checker(self):
        cheker = CheckMigrationProducts()
        return cheker

    def test_verify_create_product(self, checker):
        num_products = Product.objects.count()
        migration = SapMigration.objects.create()
        counter = 10
        for item in range(1, counter):
            SapMigrationDetail.objects.create(
                account_code='00877765445{}'.format(item),
                name='test_{}'.format(item),
                quantity_per_box=6,
                ean_13_code='00877765445{}'.format(item),
                health_register='RH_{}-01-2'.format(item),
                id_sap_migration=migration
            )

        checker.verify(migration.pk)
        assert Product.objects.count() > num_products
        assert (Product.objects.count() - num_products) == counter-1

    def test_verify_not_create_product(self, checker):
        num_products = Product.objects.count()
        checker.verify(1)
        assert Product.objects.count() == num_products
