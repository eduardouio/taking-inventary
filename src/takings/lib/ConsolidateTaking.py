import json

from django.db.models import Sum

from products.models import Product
from sap_migrations.lib.CheckMigrationProducts import CheckMigrationProducts
from sap_migrations.models import SapMigrationDetail
from takings.models import Taking


class ConsolidateTaking(object):
    """
    consolida los datos de una tomar de inventario
        report : [
            { 
                'product': '01012093780121020750', 
                'total_onhand': 0, 
                'taking': 0, 
                'pending': 0, 
                'is_complete': False | True, 
            },
        ]  # para cada uno de los items
    """

    def get(self, id_taking) -> list:
        taking = Taking.get(id_taking)
        
        if not taking:
            raise Exception('No existe la toma de inventario')
        
        return self.get_init_stock(taking)

    def get_init_stock(self, taking):
        # verificamos que los productos existan
        CheckMigrationProducts().verify(taking.id_sap_migration)

        # obtenemos los productos de las bodegas
        warenhouses = json.loads(taking.warenhouses)
        products = Product.objects.all()

        # obtenemos los items de las bodegas, y agrupamos por producto
        stock_report = SapMigrationDetail.objects.filter(
            id_sap_migration=taking.id_sap_migration,
        ).filter(
            warenhouse_name__in=warenhouses
            ).values(
            'account_code'
        ).annotate(
            total_onhand=Sum('on_hand')
        )

        stock_report = [{
            'account_code': item['account_code'],
            'total_onhand': item['total_onhand'],
            'product': '',
            'ean_13_code': '',
            'capacity': '',
            'quantity_per_box': '',
            'taking': 0,
            'pending': 0,
            'is_complete': False,
            'type_product': '',
        } for item in stock_report]

        for sku in stock_report:
            for product in products:
                if sku['account_code'] == product.account_code:
                    sku['type_product'] = product.type_product.split(';')[0] if product.type_product else 'LICORES'
                    sku['product'] = product.name
                    sku['ean_13_code'] = product.ean_13_code
                    sku['capacity'] = product.capacity
                    sku['quantity_per_box'] = product.quantity_per_box
                    break
        
        # Verificamos la categorias
        categories = json.loads(
                        taking.categories
                    ) if taking.categories else None
        
        # si existen categorias, filtramos por ellas
        if categories and categories[0] != 'ALL':
            return [i for i in stock_report if i['type_product'] in categories]
        
        return stock_report
        
    def get_takings(self, id_taking):
        pass


