from django.test import TestCase
from warenhouses.models import Warenhouse


class TestWarenhouseModel(TestCase):

    def test_get_by_owner(self):
        spected_data = [
            'Almacén General UIO.',
            'Almagro Bodega Fiscal',
            'BODEGA CONSIGNACIONES CLIENTES',
            'Bodega Cordovez - Carcelén',
            'Consignaciones Plusbrand',
            'Consignaciones Servmultimarc',
            'Control de Calidad Carcelen',
            'Control de Calidad Matriz',
            'Etiquetas CFS',
            'Vitrina',
        ]

        warenhouses = Warenhouse.get_by_owner(
            'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.'
        )
        warenhouses_db = [item.name for item in warenhouses]
        self.assertEqual(spected_data, warenhouses_db)
        self.assertEqual(len(spected_data), len(warenhouses_db))

    def test_get_owners(self):
        spected_data = {
            'name': 'Almacén General UIO.',
            'owners': [
                'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.',
                'IMNAC IMPORTADORA NACIONAL CIA LTDA',
                'REV ECUADOR S.A'
            ]
        }
        owners =  Warenhouse.get_owners(spected_data['name'])
        self.assertEqual(spected_data['owners'], owners )
        self.assertEqual(len(spected_data['owners']), len(owners))

    def test_get_by_name(self):
        my_warenhouse = Warenhouse.get_by_name('Almacen de Consignacion')
        self.assertIsInstance(my_warenhouse, Warenhouse)
        self.assertEqual(my_warenhouse.name, 'Almacen de Consignacion')
        self.assertEqual(my_warenhouse.id_warenhouse_sap_code, '03')

        not_found_warenhouse = Warenhouse.get_by_name('Doesn not exist')
        self.assertIsNone(not_found_warenhouse)