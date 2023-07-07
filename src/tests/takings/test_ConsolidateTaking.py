import pytest
from takings.lib import ConsolidateTaking
from takings.models import Taking
import json


@pytest.mark.django_db
class TestConsolidateTaking:

    def test_get_one_warernhouse_all_categories(self):
        # toma 175 y migracion 180
        # categorias null -> Todas
        resume_taking = ConsolidateTaking().get(175)
        taking = Taking.get(175)
        spected_data = {
            'taking': taking,
            'warenhouses': ['LAGUARDA CUENCA'],
            'total_products': 807,
            'total_by_categories': {
                'LICORES': 7060,
                'VARIOS': 469,
                'ACCESORIOS': 250,
            },
            'enterprises': ['CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.'],
            "sample_products": [
                {'account_code': '08022272402101020200', 'on_hand': 6,
                    'on_order': 0, 'is_commited': 0, 'avaliable': 6},
                {'account_code': '11012133910105010200', 'on_hand': 20,
                    'on_order': 0, 'is_commited': 0, 'avaliable': 20},
                {'account_code': '08022272402101010100', 'on_hand': 13,
                 'on_order': 0, 'is_commited': 0, 'avaliable': 13},
                {'account_code': '07015932404102010000', 'on_hand': 28,
                 'on_order': 0, 'is_commited': 0, 'avaliable': 28},
                {'account_code': '11012133910101010200', 'on_hand': 30,
                 'on_order': 0, 'is_commited': 0, 'avaliable': 30},

            ]
        }

        assert resume_taking['taking'] == taking

        # comprobamos los items de la toma
        for item in resume_taking['report']:
            for spected_item in spected_data['sample_products']:
                if item['account_code'] == spected_item['account_code']:
                    assert item['on_hand'] == spected_item['on_hand']
                    assert item['on_order'] == spected_item['on_order']
                    assert item['is_commited'] == spected_item['is_commited']
                    assert item['avaliable'] == spected_item['avaliable']

        # comprobamos las bodegas
        assert json.loads(taking.warenhouses) == spected_data['warenhouses']

        # comprobamos las categorias y cantidades
        report = resume_taking['report']
        for spc_category in spected_data['total_by_categories']:
            assert (
                spected_data['total_by_categories'][spc_category]
                ==
                sum([i['on_hand']
                    for i in report if i['category'] == spc_category])
            )

        # comprobamos las empresas

        # comprobamos las tomas

    def test_not_exist_taking(self):
        resume_taking = ConsolidateTaking().get(9999999)
        assert resume_taking == False
