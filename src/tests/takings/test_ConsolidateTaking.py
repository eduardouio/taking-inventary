from django.test import TestCase
from takings.lib import ConsolidateTaking
from products.models import Product

class TestConsolidate(TestCase):

    def setUp(self):
        self.consolidate = ConsolidateTaking()
        return super().setUp()
    
    def test_report(self):
        warenhouses = [
            'Almacén general UIO'
        ]

        product = Product.get('02012130020202010750')
        spected_report = {
                'sku_code': '02012130020202010750',
                'porduct': product,
                'sap_stock': 4623,
                'tk_bottles': 25,
                'tk_boxes': 3939,
                'tk_quantity': 47293,
                'is_complete': False, 
            }
        report = self.consolidate.get(69)
        for item in report['report']:
            if item['account_code'].account_code == product.account_code:
                self.assertEqual(spected_report['tk_bottles'], item['tk_bottles'])
                self.assertEqual(spected_report['tk_boxes'], item['tk_boxes'])
                self.assertEqual(spected_report['tk_quantity'], item['tk_quantity'])
                self.assertEqual(spected_report['sap_stock'], item['sap_stock'])
                self.assertEqual(spected_report['sku_code'], item['sku_code'])
                self.assertIsInstance(item['product'], Product)

        warenhouses = ''
    def test_does_not_exist(self):
        self.assertIsNone(self.consolidate.get(169))