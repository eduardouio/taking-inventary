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

    def  test_by_warenhouse(self):
        sample_spected_data = {
            'account_code':'01022020080101010200',
            'name':'CHAMPAGNE HENKELL PICCOLO DRY',
            'columns': [{
                	'name': 'ALMACEN 10 DE AGOSTO',
                	'on_hand': 418,
                	'on_order': 455,
                	'is_commited':18,
                	'avaliable': 855
                },{
                	'name': 'ALMACÉN GENERAL UIO',
                	'on_hand': 421,
                	'on_order': 104,
                	'is_commited':11,
                	'avaliable': 514
                },{
                	'name': 'Almacén General UIO.',
                	'on_hand': 406,
                	'on_order': 45,
                	'is_commited':15,
                	'avaliable': 436
                },{
                	'name': 'BODEGA CARCELEN',
                	'on_hand': 1,
                	'on_order': 231,
                	'is_commited':14,
                	'avaliable': 218,
                },{
                	'name': 'BODEGA CONSIGNACIONES CLIENTES',
                	'on_hand': 85,
                	'on_order': 707,
                	'is_commited':45,
                	'avaliable': 747
                },{
                	'name': 'BODEGA CUENCA',
                	'on_hand': 120,
                	'on_order': 221,
                	'is_commited':11,
                	'avaliable': 330
                },{
                	'name': 'Bodega General G8',
                	'on_hand': 316,
                	'on_order': 322,
                	'is_commited':46,
                	'avaliable': 592
                },{
                	'name': 'General GYE',
                	'on_hand': 183,
                	'on_order': 250,
                	'is_commited':21,
                	'avaliable': 412
                },{
                	'name': 'LAGUARDA',
                	'on_hand': 99,
                	'on_order': 237,
                	'is_commited':43,
                	'avaliable': 293
                },{
                	'name': 'LAGUARDA CUMBAYA',
                	'on_hand': 16,
                	'on_order': 102,
                	'is_commited':-1,
                	'avaliable': 119
                },{
                	'name': 'LAGUARDA MANTA',
                	'on_hand': 6,
                	'on_order': 214,
                	'is_commited':13,
                	'avaliable': 207
                },{
                	'name': 'LAGUARDA PORTUGAL',
                	'on_hand': 149,
                	'on_order': 5,
                	'is_commited':27,
                	'avaliable': 127
                },{
                	'name': 'LAGUARDA SAMBORONDON',
                	'on_hand': 333,
                	'on_order': 325,
                	'is_commited':35,
                	'avaliable': 623
                },{
                	'name': 'LAGUARDA VIA LA COSTA',
                	'on_hand': 407,
                	'on_order': 388,
                	'is_commited':-1,
                	'avaliable': 796
                },{
                	'name': 'MATRIZ PLUSBRAND',
                	'on_hand': 258,
                	'on_order': 368,
                	'is_commited':0,
                	'avaliable': 626
                },{
                	'name': 'MATRIZ PLUSBRAND CUENCA',
                	'on_hand': 476,
                	'on_order': 303,
                	'is_commited':37,
                	'avaliable': 742
                },{
                	'name': 'MATRIZ PLUSBRAND GYE',
                	'on_hand': 373,
                	'on_order': 275,
                	'is_commited':1,
                	'avaliable': 647
                },
                {
                	'name': 'MATRIZ PLUSBRAND MANTA',
                	'on_hand': 178,
                	'on_order': 281,
                	'is_commited':27,
                	'avaliable': 432
                },{
                	'name': 'Vitrina',
                	'on_hand': 271,
                	'on_order': 45,
                	'is_commited':15,
                	'avaliable': 301
                }]}
        report = self.consolidateMigration.get(1)
        for warenhouse in report['table_by_warenhouses']:
            if warenhouse['account_code'] == sample_spected_data['account_code']:
                for spected_whrs in sample_spected_data['columns']:
                    for whrs in warenhouse['columns']:
                        if whrs['name'] == spected_whrs['name']:
                            self.assertEqual(
                                whrs['on_hand'],spected_whrs['on_hand']
                            )
                            self.assertEqual(
                                whrs['is_commited'],spected_whrs['is_commited']
                            )
                            self.assertEqual(
                                whrs['on_order'],spected_whrs['on_order']
                            )
                            self.assertEqual(
                                whrs['avaliable'],spected_whrs['avaliable']
                            )

    def  test_by_warenhouse(self):
        sample_spected_data = {
            'account_code':'01011010010206010750',
            'name':'VINO TINTO RESERVADO MALBEC',
            'columns': [{
                    'name':'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.',
                    'on_hand': 923,
                    'on_order': 604,
                    'is_commited': 82,
                    'avaliable': 1445,
                },{
                    'name':'CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.',
                    'on_hand': 2137,
                    'on_order': 1757,
                    'is_commited': 218,
                    'avaliable': 3676,
                },{
                    'name':'SERVMULTIMARC CIA. LTDA.',
                    'on_hand': 1181,
                    'on_order': 1490,
                    'is_commited': 86,
                    'avaliable': 2585,
                },{
                    'name':'VINOS Y ESPIRITUOSOS DEL LITORAL VINLITORAL S.A.',
                    'on_hand': 187,
                    'on_order': 229,
                    'is_commited': 12,
                    'avaliable': 404,
                },{
                    'name':'VINOS Y ESPIRITUOSOS VINESA S.A',
                    'on_hand': 1192,
                    'on_order': 858,
                    'is_commited': 77,
                    'avaliable': 1973,
                }
            ], }

        report = self.consolidateMigration.get(1)
        for owner in report['table_by_owners']:
            if owner['account_code'] == sample_spected_data['account_code']:
                for spected_whrs in sample_spected_data['columns']:
                    for ownr in owner['columns']:
                        if ownr['name'] == spected_whrs['name']:
                            self.assertEqual(
                                ownr['on_hand'],spected_whrs['on_hand']
                            )
                            self.assertEqual(
                                ownr['is_commited'],spected_whrs['is_commited']
                            )
                            self.assertEqual(
                                ownr['on_order'],spected_whrs['on_order']
                            )
                            self.assertEqual(
                                ownr['avaliable'],spected_whrs['avaliable']
                            )