import json
import pandas as pd

from products.models import Product
from takings.models import Taking
from sap_migrations.models import SapMigrationDetail


class ConsolidateTaking(object):

    def get(self, id_taking):
        """Resumen del stock inicial cruzado con las tomas"""
        taking = Taking.get(id_taking)
        if not taking:
            return False

        # obtenemos el stock inicial
        owners, start_stock = self.get_start_stock(taking)
        taking_report = self.get_takings(taking, start_stock)

        return {
            'report': taking_report,
            'taking': taking,
            'owners': owners,
        }

    def get_takings(self, taking, start_stock):
        """retona las tomas de los items"""
        pass

    def get_start_stock(self, taking):
        """Stock inicial"""
        # definimos bodegas y categorias
        warenhouses = json.loads(taking.warenhouses)
        categories = json.loads(taking.categories
                                ) if taking.categories else ['ALL']

        migration_detail = SapMigrationDetail.objects.filter(
            id_sap_migration=taking.id_sap_migration,
        ).filter(warenhouse_name__in=warenhouses)

        data_frame = []
        start_stock = []
        owners = []

        for item in migration_detail:
            data_frame.append({
                'account_code': item.account_code,
                'is_commited': item.is_commited,
                'on_order': item.on_order,
                'avaliable': item.avaliable,
                'on_hand': item.on_hand,
                'owners': item.company_name,
            })

        owners = list(set([i['owners'] for i in data_frame]))
        df = pd.DataFrame(data_frame)
        df = df.groupby('account_code').sum().reset_index()

        for _, row in df.iterrows():
            start_stock.append({
                'account_code': row['account_code'],
                'is_commited': row['is_commited'],
                'on_order': row['on_order'],
                'avaliable': row['avaliable'],
                'on_hand': row['on_hand'],
            })
        # verificamos los productos en la base de datos
        all_products = Product.objects.all()
        for product in all_products:

            category = product.type_product.split(
                ';')[0] if product.type_product else 'LICORES'

            for stock in start_stock:
                if product.account_code == stock['account_code']:
                    stock['product_name'] = product.name
                    stock['category'] = category

        # filtramos las categorias
        categories = json.loads(taking.categories) if taking.categories else []

        if categories:
            start_stock = [
                stock
                for stock
                in start_stock if stock['category'] in categories
            ]

        return owners, start_stock
