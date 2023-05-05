import json
import pandas as pd
from django_pandas.io import read_frame

from django.core.serializers import serialize

from sap_migrations.models import SapMigration, SapMigrationDetail
from products.models import Product


class ConsolidateMigration(object):

    def get(self, id_sap_migration):
        # obtenemos los detalles de la migracion de SAP
        sap_migration = SapMigration.get(id_sap_migration)
        sap_migration_detail = SapMigrationDetail.objects.filter(
            id_sap_migration=sap_migration
        )
        # convertimos los detalles de la migracion en un dataframe
        df = read_frame(sap_migration_detail)

        # agrupamos los detalles de la migracion
        report = {
            "by_company_name": json.loads(
                df.groupby(["account_code", "company_name"])[[
                    "on_hand",
                    "on_order",
                    "is_commited",
                    "avaliable"
                ]].sum().to_json()),
            "by_account_code": json.loads(
                df.groupby(["account_code", "name"])[[
                    "on_hand",
                    "on_order",
                    "is_commited",
                    "avaliable"
                ]].sum().to_json()),
            "by_warenhouse_name": json.loads(
                df.groupby(["account_code", "warenhouse_name"])[[
                    "on_hand",
                    "on_order",
                    "is_commited",
                    "avaliable"
                ]].sum().to_json()),
        }
        return self._make_dict(report)

    def _make_dict(self, report):
        # creamos un arreglo para cada agrupacion
        report_data = {
            'by_company_name': [],
            'by_account_code': [],
            'by_warenhouse_name': []
        }
        products = Product.objects.all()
        for by_condition in report.keys():
            for (item, on_hand, on_order, is_commited, avaliable) in zip(
                    report[by_condition]['on_hand'],
                    report[by_condition]['on_hand'].values(),
                    report[by_condition]['on_order'].values(),
                    report[by_condition]['is_commited'].values(),
                    report[by_condition]['avaliable'].values(),
            ):
                product_info = item.replace(")", "").replace(
                    "(", "").replace("'", "").split(",")
                product = self._get_product(
                    product_info[0].strip(), products
                )
                report_data[by_condition].append({
                    "company": product_info[1].strip(),
                    "account_code": product_info[0].strip(),
                    "name": product.name,
                    "on_hand": on_hand,
                    "on_order": on_order,
                    "is_commited": is_commited,
                    "avaliable": avaliable,
                })
        return report_data

    def _get_product(self, account_code, products):
        for product in products:
            if product.account_code == account_code:
                return product
        # si el producto no existe lo crea
        detail = SapMigrationDetail.objects.filter(
            account_code=account_code
        ).first()

        if not detail:
            raise Exception('Error al obtener el detalle de la migracion')

        product = Product.objects.create(
            account_code=detail.account_code,
            name=detail.name,
            quantity_per_box=detail.quantity_per_box,
            ean_13_code=detail.ean_13_code,
            health_register=detail.health_register,
        )
        return product
