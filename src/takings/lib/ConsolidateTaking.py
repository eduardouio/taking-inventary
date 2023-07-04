import json
from django.db import connection

from products.models import Product
from takings.models import Taking
from sap_migrations.models import SapMigrationDetail


class ConsolidateTaking(object):

    def get(self, id_taking):
        taking = Taking.get(id_taking)
        if taking is None:
            return None

        start_stock, warenhouses = self.get_start_stock(taking)
        taking_resume = self.get_resume_taking(id_taking)
        for sku_stock in start_stock:
            sku_stock['product'] = Product.get(
                sku_stock['account_code'].account_code
            )

            # colocamos toma incial en 0
            sku_stock['is_complete'] = False
            sku_stock['tk_bottles'] = 0
            sku_stock['tk_boxes'] = 0
            sku_stock['tk_quantity'] = 0

            # verificamos que el producto exista, sino lo creamos
            if sku_stock['product'] is None:
                sku_stock['product'] = Product.objects.create(
                    name=sku_stock['account_code'].name,
                    account_code=sku_stock['account_code'].account_code,
                    quantity_per_box=sku_stock['account_code'].quantity_per_box,
                    ean_13_code=sku_stock['account_code'].ean_13_code,
                    type_product='LICORES;VARIOS',
                )

            sku_stock['diff'] = sku_stock['sap_stock']

            for tkn_stock in taking_resume:
                item_found = False
                if sku_stock['account_code'].account_code == tkn_stock['account_code']:
                    sku_stock['sku_code'] = tkn_stock['account_code']
                    sku_stock['diff'] = int(
                        tkn_stock['quantity']) - sku_stock['sap_stock']

                    sku_stock['is_complete'] = False

                    if sku_stock['sap_stock'] == int(tkn_stock['quantity']):
                        sku_stock['is_complete'] = True

                    sku_stock['tk_bottles'] = int(
                        tkn_stock['taking_total_bottles'])
                    sku_stock['tk_boxes'] = int(
                        tkn_stock['taking_total_boxes'])
                    sku_stock['tk_quantity'] = int(tkn_stock['quantity'])
                    item_found = True
                    break

                if item_found is False:
                    sku_stock['sku_code'] = tkn_stock['account_code']
                    sku_stock['is_complete'] = False
                    sku_stock['tk_bottles'] = 0
                    sku_stock['tk_boxes'] = 0
                    sku_stock['tk_quantity'] = 0

        enterprises = self.get_owners(taking.id_sap_migration_id, warenhouses)
        return {
            'report': start_stock,
            'taking': taking,
            'warenhouses': warenhouses,
            'enterprises': enterprises,
        }

    def get_resume_taking(self, id_taking):
        cursor = connection.cursor()
        cursor.execute('''
                SELECT 
                    pp.account_code,
                    SUM(tt.taking_total_bottles) taking_total_bottles,
                    SUM(tt.taking_total_boxes) taking_total_boxes,
                    SUM(tt.quantity) quantity 
                FROM takings_takindetail tt 
                LEFT JOIN products_product pp ON (
                        pp.id_product = tt.account_code_id
                )
                WHERE tt.id_taking_id = {}
                GROUP BY pp.account_code ;
        '''.format(id_taking))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get_start_stock(self, taking):
        # segramos las bodegas y por categoria
        report = []
        warenhouses = list(set(json.loads(taking.warenhouses)))

        for warenhouse in warenhouses:
            detail = SapMigrationDetail.get_by_warenhouse_name(
                taking.id_sap_migration_id, warenhouse
            )
            if detail:
                report.extend(detail)

        products = list(set([i.account_code for i in report]))
        resume = []

        for product in products:
            resume_item = {
                'account_code': None,
                'sap_stock': 0,
            }

            for item in report:
                if item.account_code == product:
                    resume_item['account_code'] = item
                    resume_item['sap_stock'] += item.on_hand

            resume.append(resume_item)

        return resume, warenhouses

    def get_owners(self, id_sap_migration, warenhouses):
        enterprises = []
        cursor = connection.cursor()

        for warenhouse in warenhouses:
            cursor.execute('''
                SELECT 
                    DISTINCT(sms.company_name)
                FROM 
                    sap_migrations_sapmigrationdetail sms 
                WHERE 
                    sms.id_sap_migration_id  = {} and sms.warenhouse_name  = '{}';
            '''.format(id_sap_migration, warenhouse))

            columns = [col[0] for col in cursor.description]
            enterprises.extend([
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ])

        enterprises = list(set([x['company_name'] for x in enterprises]))

        return enterprises
