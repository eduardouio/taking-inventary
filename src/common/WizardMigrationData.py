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

    def run_query(self, query, many_columns=False):
        cursor = connection.cursor()
        cursor.execute(query)
        if many_columns:
            data = [list(row) for row in cursor.fetchall()]
        else:
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
        all_users = [
            {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'selected': False
            } for user in all_users
        ]

        # listado de almacenes
        warenhouses_names = self.run_query(
            """SELECT DISTINCT(sms.warenhouse_name) 
            FROM sap_migrations_sapmigrationdetail sms 
            WHERE  sms.id_sap_migration_id = {}
            ORDER BY sms.warenhouse_name""".format(id_sap_migration)
        )
        # listado de propietarios de las bodegas
        warenhouses_owners = []
        for warenhouse in warenhouses_names:
            owners = self.run_query(
                """
                SELECT  DISTINCT(sms.company_name)
                FROM sap_migrations_sapmigrationdetail sms  
                WHERE  sms.id_sap_migration_id = {}
                AND sms.warenhouse_name  = '{}'
                """.format(id_sap_migration, warenhouse)
            )
            warenhouses_owners.append({
                'warenhouse_name': warenhouse,
                'owners': owners
            })

        # listado de tipos de productos
        type_products = self.run_query(
            """SELECT DISTINCT(pp.type_product) 
            FROM products_product pp
            ORDER BY pp.type_product"""
        )

        # generemos el diccionario de datos de productos
        type_products = [{'type_product': tp, "selected": False}
                         for tp in type_products if tp is not None
                         ]

        # listado de prductos
        products = self.run_query("""
                SELECT DISTINCT(account_code), "name", false AS selected 
                FROM sap_migrations_sapmigrationdetail 
                WHERE id_sap_migration_id = {} order by "name"
        """.format(id_sap_migration), many_columns=True)

        products = [
            dict(zip(['account_code', 'name', 'selected'], product))
            for product in products
        ]

        return {
            'sap_migration': sap_migration,
            'warenhouses': warenhouses_names,
            'warenhouses_owners': warenhouses_owners,
            'type_products': type_products,
            'all_users': all_users,
            'products': products,
        }
