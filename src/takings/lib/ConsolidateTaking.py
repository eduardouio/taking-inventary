import json

from django.db.models import Sum

from products.models import Product
from sap_migrations.lib.CheckMigrationProducts import CheckMigrationProducts
from sap_migrations.models import SapMigrationDetail
from takings.models import Taking, TakinDetail


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

    def __init__(self):
        self.products = Product.objects.all()
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
            'id_product': 0,
            'type_product': '',
            'product': '',
            'ean_13_code': '',
            'quantity_per_box': '',
            'capacity': '',
            'total_onhand': item['total_onhand'],
            'taking': 0,
            'pending': 0,
            'is_complete': False,
        } for item in stock_report]

        for sku in stock_report:
            for product in self.products:
                if  sku['account_code'] == product.account_code:
                    sku['id_product'] = product.pk
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
            stock_report =  [i for i in stock_report if i['type_product'] in categories]
            return self.get_takings(stock_report, taking)
        
        return  self.get_takings(stock_report, taking)
        
    def get_takings(self, stock_report, taking):
        # recuperamos las tomas del reporte
        taking_report = TakinDetail.objects.filter(
            id_taking_id=taking.pk
        ).values(
            'account_code_id'
        ).annotate(
            quantity=Sum('quantity')
        )

        if not taking_report:
            return stock_report

        for item in stock_report:
            for taking in taking_report:
                if item['id_product'] == taking['account_code_id']:
                    item['taking'] = taking['quantity']
                    item['pending'] = item['total_onhand'] - taking['quantity']
                    item['is_complete'] = True if item['pending'] == 0 else False
                    break

        return stock_report
