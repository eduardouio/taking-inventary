from products.models import Product
from sap_migrations.models import SapMigrationDetail


class CheckMigrationProducts():
    """Comprueba que los productos de la migracion existan en el sistema,
    sio lo crea"""

    def verify(self, id_sap_migration):

        details = SapMigrationDetail.objects.filter(
            id_sap_migration_id=id_sap_migration
        ).values_list('account_code', flat=True).distinct()

        for account_code in details:
            if Product.get(account_code) is None:
                new_product = SapMigrationDetail.objects.filter(
                    account_code=account_code
                ).first()
                Product.objects.create(
                    account_code=account_code,
                    name=new_product.name,
                    quantity_per_box=new_product.quantity_per_box,
                    ean_13_code=new_product.ean_13_code,
                    notes=new_product.health_register,
                )
