import json

from accounts.models.CustomUserModel import CustomUserModel
from django.db import connection


from sap_migrations.models import SapMigration
from api.Serializers import CustomUserSerializer, SapMigrationSerializer


class WizardMigrationData:
    """
        Obtiene un diccionario con los datos necesarios para el wizard de 
        toma de una migración de SAP
    """

    def run_query(self, query):
        cursor = connection.cursor()
        cursor.execute(query)
        data = [list(row)[0] for row in cursor.fetchall()]
        return data

    def get(self, id_sap_migration):
        sap_migration = SapMigration.get(id_sap_migration)

        if sap_migration is None:
            raise Exception(
                'No existe la migración de SAP con id: {}'.format(
                    id_sap_migration)
            )

        # listado de usuarios con perfil asistentes
        all_users = CustomUserModel.objects.filter(
            role='asistente'
        )

        # listado de almacenes
        warenhouses_names = self.run_query(
            """SELECT DISTINCT(sms.warenhouse_name) 
            FROM sap_migrations_sapmigrationdetail sms 
            WHERE  sms.id_sap_migration_id = {}
            ORDER BY sms.warenhouse_name""".format(id_sap_migration)
        )

        # listado de tipos de productos
        type_products = self.run_query(
            """SELECT DISTINCT(pp.type_product) 
            FROM products_product pp
            ORDER BY pp.type_product"""
        )

        return {
            'sap_migration': sap_migration,
            'warenhouses': warenhouses_names,
            'type_products': type_products,
            'all_users': all_users
        }
