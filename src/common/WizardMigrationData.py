from products.models import Product
from sap_migrations.models import SapMigration, SapMigrationDetail
from accounts.models.CustomUserModel import CustomUserModel


class WizardMigrationData:
    """
        Obtiene un diccionario con los datos necesarios para el wizard de 
        toma de una migración de SAP
    """

    def get(self, id_sap_migration):
        sap_migration = SapMigration.get(id_sap_migration)

        if sap_migration is None:
            raise Exception(
                'No existe la migración de SAP con id: ' + id_sap_migration
            )

        # listado de usuarios con perfil asistentes
        all_users = CustomUserModel.objects.filter(
            role='asistente'
        )

        # listado de almacenes
        warenhouses_names = SapMigrationDetail.objects.filter(
            id_sap_migration=sap_migration
        ).values_list('warenhouse_name', flat=True).distinct()

        # listado de tipos de productos
        types_product = Product.objects.all()

        # datos del wizard
        wizard_data = {
            'sap_migration': sap_migration,
            'warenhouses': warenhouses_names,
            'types_products': types_product,
            'all_users': all_users,
        }

        # retorna los datos del wizard
        return wizard_data
