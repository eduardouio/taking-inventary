from django.test import TestCase
from sap_migrations.lib import ConsolidateMigration 
from sap_migrations.models import SapMigration, SapMigrationDetail

class Test_ConsolidateMigrations(TestCase):

    def setUp(self) -> None:
        self.consolidateMigration = ConsolidateMigration()
        return super().setUp()

    def test__get_init_report(self):
        spected_data = {
            'total_owners': 8,
            'total_on_hand': 2933786,
            'total_on_order': 2937016,
            'total_is_commited': 286777,
            'total_avaliable': 5584025,
            'total_products': 1473
        }

        report = self.consolidateMigration.get(1)
        self.assertEqual(
            spected_data['total_on_order'],
            report['totals']['on_order']
        )
        self.assertEqual(
            spected_data['total_on_hand'], 
            report['totals']['on_hand']
        )
        self.assertEqual(
            spected_data['total_is_commited'], 
            report['totals']['is_commited']
        )
        self.assertEqual(
            spected_data['total_avaliable'], 
            report['totals']['avaliable']
        )

        self.assertIsInstance(report['sap_migration'], SapMigration)

        self.assertTrue(report['status'])
        self.assertEqual(
            len(report['by_products']),
            spected_data['total_products']
        )
    
    def test_by_product_no_found(self):
        spected_data = {
            'sap_migration': None,
            'sap_migration_detail': None,
            'status': False,
            'products': {},
            'warenhouses': {},
            'owners': {},
            'totals': {
                'on_hand': 0,
                'on_order': 0,
                'is_commited': 0,
                'avaliable': 0,
            },
        }

        report = self.consolidateMigration.get(1000)
        self.assertDictEqual(spected_data, report)

    
    def test_by_products(self):
        report = self.consolidateMigration.get(1)
        spected = {
            'by_products': {
                'header': '01012244950102010750',
                'total_lines_report': 4,
                'totals': {
                    'on_hand': 835,
                    'on_order':1132,
                    'is_commited': 116, 
                    'avaliable': 1851,
             },
            'by_warenhouses': {
                'header': 'Almacén General UIO.',
                'total_lines_report': 406,
                'totals': {
                    'on_hand': 100608,
                    'on_order': 102347,
                    'is_commited': 9785,
                    'avaliable': 193170,
                }
            },
            'by_owners': {
                'header': 'REV ECUADOR S.A',
                'total_lines_report': 19,
                'totals': {
                    'on_hand': 4497,
                    'on_order': 4896,
                    'is_commited': 414,
                    'avaliable': 8979,
                }
                    },
            }}

        for type_test in spected:
            specific_report  = report[type_test]
            for spd_rpt in specific_report:
                if [*spd_rpt][0] == spected[type_test]['header']:
                    self.assertDictEqual(
                        spected[type_test]['totals'],
                        spd_rpt['totals']
                    )
                    self.assertEqual(
                        len(spd_rpt[spected[type_test]['header']]),
                        spected[type_test]['total_lines_report']
                    )

        sap_migration = SapMigration.get(1)
        self.assertTrue(sap_migration.have_report)