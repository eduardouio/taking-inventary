from django.test import TestCase
from sap_migrations.lib import ConsolidateMigration 
from products.models import Product
from sap_migrations.models import SapMigration, SapMigrationDetail

class Test_ConsolidateMigrations(TestCase):

    def setUp(self) -> None:
        self.consolidateMigration = ConsolidateMigration()
        return super().setUp()

    def test_get_by_all_products(self):
        spected_data = {
            'total_enterprises': 8,
            'total_on_hand': 2933786,
            'total_on_order': 2937016,
            'total_is_commited': 286777,
            'total_avaliable': 5584025,
            'total_line_items': 11724,
            'total_products': 1473
        }

        report = self.consolidateMigration.get(1)
        self.assertEqual(
            spected_data['total_on_order'],
            report['total_on_order']
        )
        self.assertEqual(
            spected_data['total_on_hand'], 
            report['total_on_hand']
        )
        self.assertEqual(
            spected_data['total_is_commited'], 
            report['total_is_commited']
        )
        self.assertEqual(
            spected_data['total_avaliable'], 
            report['total_avaliable']
        )
        self.assertEqual(
            spected_data['total_line_items'],
            len(report['sap_migration_detail'])
        )
        self.assertIsInstance(report['sap_migration'], SapMigration)
        self.assertIsInstance(
            report['sap_migration_detail'][0],
            SapMigrationDetail
        )
        self.assertTrue(report['status'])
        # product by results
        by_product_spected = {
            'account_code': Product.get('01012244950102010750'),
            'total_lines_report': 4,
            'totals': {
                'total_on_hand': 835,
                'total_on_order':1132,
                'total_is_commited': 116, 
                'total_avaliable': 1851,
            }
        }

        for line_item in report['by_products']:
            if line_item['product'] == by_product_spected['account_code']:
                self.assertDictEqual(
                    line_item['totals'],
                    by_product_spected['totals']
                )
                self.assertEqual(
                    len(line_item['items']), 
                    by_product_spected['total_lines_report']
                )
        self.assertEqual(
            len(report['by_products']),
            spected_data['total_products']
        )

    def test_by_product_no_found(self):
        spected_data = {
            'sap_migration': None,
            'sap_migration_detail':None,
            'products': {},
            'warenhouses':{},
            'owners': {},
            'total_on_hand': 0,
            'total_on_order': 0,
            'total_is_commited': 0,
            'total_avaliable': 0,
            'status': False,
            'message': 'Migracion sin items'
        }

        report = self.consolidateMigration.get(1000)
        self.assertDictEqual( spected_data,report )

    def test_by_warenhouse(self):
        # TODO testear por bodega y por empresa
        pass