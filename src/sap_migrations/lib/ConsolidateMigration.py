from django.core.serializers import serialize
from sap_migrations.models import SapMigration, SapMigrationDetail
from products.models import Product
from django.db import connection
import json
from time import time


class ConsolidateMigration(object):

    def __init__(self):
        self.sap_migration = None

    def get(self, migration_id):
        inital = time()
        self.sap_migration = SapMigration.get(migration_id)
        report = {
            'sap_migration': self.sap_migration,
            'sap_migration_detail': SapMigrationDetail.get_by_migration(migration_id),
            'by_products': [],
            'warenhouses': {},
            'status': False,
        }
        if self.sap_migration is None:
            return report
        all_products = Product.objects.all()
        report['by_products'] = self.run_query('''
                SELECT 
                    sms.account_code,
                	SUM(sms.on_hand) on_hand,
                	SUM(sms.on_order) on_order,
                	SUM(sms.is_commited) is_commited,
                	SUM(sms.avaliable) avaliable
                FROM sap_migrations_sapmigrationdetail sms 
                WHERE sms.id_sap_migration_id  = {} 
                AND sms.avaliable > 0
                GROUP BY sms.account_code
        '''.format(self.sap_migration.pk))

        for sku_item in report['by_products']:
            for product in all_products:
                if product.account_code == sku_item['account_code']:
                    sku_item['name'] = product.name

        for item in report['sap_migration_detail']:
            import ipdb;ipdb.set_trace()
            report['warenhouses'][item['warenhouse_name']] = item['id_warenhouse_sap_code']
            


    def run_query(self, sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]