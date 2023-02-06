import json
from django.db import connection

from products.models import Product
from takings.models import TakinDetail, Taking
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
            sku_stock['diff'] = sku_stock['sap_stock']
            for tkn_stock in taking_resume:
                if sku_stock['account_code'].account_code == tkn_stock['account_code']:
                    sku_stock['sku_code'] = tkn_stock['account_code']
                    sku_stock['diff'] = sku_stock['sap_stock'] - \
                        int(tkn_stock['quantity'])

                    if sku_stock['product'] is None:
                        raise Exception('Dont exist {} in db'.format(
                            tkn_stock['account_code']))

                    sku_stock['is_complete'] = False

                    if sku_stock['sap_stock'] == int(tkn_stock['quantity']):
                        sku_stock['is_complete'] = True
                    sku_stock['tk_bottles'] = int(
                        tkn_stock['taking_total_bottles'])
                    sku_stock['tk_boxes'] = int(
                        tkn_stock['taking_total_boxes'])
                    sku_stock['tk_quantity'] = int(tkn_stock['quantity'])
                    break
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
                    sms.id_sap_migration_id  = 14 and sms.warenhouse_name  = '{}';
            '''.format(warenhouse))

            columns = [col[0] for col in cursor.description]
            enterprises.extend([
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ])

        enterprises = list(set([x['company_name'] for x in enterprises]))

        return enterprises
