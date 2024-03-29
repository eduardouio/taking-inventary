import json

import pytest

from takings.lib import ConsolidateTaking
from takings.models import Taking, TakinDetail
from sap_migrations.models import SapMigration
from django.contrib.auth import get_user_model as UserModel


@pytest.mark.django_db
class TestConsolidateTaking:

    def test_many_warenhouses_whitout_takings(self):
        sap_migration = SapMigration.get(180)
        my_taking = Taking.objects.create(
            id_sap_migration=sap_migration,
            warenhouses=json.dumps(
                [
                    "ALMACEN 10 DE AGOSTO",
                    "ALMACÉN GENERAL UIO",
                    "BODEGA CONSIGNACIONES CLIENTES",
                    "CONSIGNACIONES PB PROVEEDORES",
                ]
            ),
            categories=json.dumps(["ALL"]),
            user_manager=UserModel().get("evillota"),
        )

        spected_data = {
            "report": {
                "items_skus": 985,
                "total_onhand": 809688,
            },
            "sample_products": [
                {
                    "account_code": "01022020080101030750",
                    "total_onhand": 1713,
                    "taking": 0,
                    "pending": 1713,
                    "is_complete": False,
                },{
                    "account_code": "02012130020202010750",
                    "total_onhand": 9522,
                    "taking": 0,
                    "pending": 9522,
                    "is_complete": False,
                },{
                    "account_code": "01012093780121020750",
                    "total_onhand": 122,
                    "taking": 0,
                    "pending": 122,
                    "is_complete": False,
                }
            ]
        }

        report = ConsolidateTaking().get(my_taking.pk)
        assert len(report) == spected_data["report"]["items_skus"]

        assert sum([item["total_onhand"] for item in report]) == spected_data["report"]["total_onhand"]

        for item in spected_data["sample_products"]:
            assert (
                    item["total_onhand"] 
                    == 
                    sum([i["total_onhand"] for i in report if i["account_code"] == item["account_code"]])
            )

    def test_get_nonexistent_taking(self):
        with pytest.raises(Exception):
            ConsolidateTaking().get(99999)

    def test_taking_by_categories(self):
        sap_migration = SapMigration.get(180)
        my_taking = Taking.objects.create(
            id_sap_migration=sap_migration,
            warenhouses=json.dumps(
                [
                    "ALMACÉN GENERAL UIO",
                    "CONSIGNACIONES PB PROVEEDORES",
                ]
            ),
            categories=json.dumps(["LICORES",]),
            user_manager=UserModel().get("evillota"),
        )

        spected_data = {
            "report": {
                "items_skus": 535,
                "total_onhand": 669728,
            },
            "sample_products": [
                {
                    "account_code": "01012093230911010750",
                    "total_onhand": 274,
                    "taking": 0,
                    "pending": 274,
                    "is_complete": False,
                },{
                    "account_code": "01011010040206010750",
                    "total_onhand": 1543,
                    "taking": 0,
                    "pending": 1543,
                    "is_complete": False,
                },{
                    "account_code": "01011080010107010750",
                    "total_onhand": 10752,
                    "taking": 0,
                    "pending": 10752,
                    "is_complete": False,
                }
            ],
            "dont_exist" : [
                {"account_code": "09012151810101020000", "categ": "ACCESORIOS"},
                {"account_code": "09012151810101020000", "categ": "ACCESORIOS"},
                {"account_code": "11012133910102010200", "categ": "VARIOS"},
                {"account_code": "11012133910103010200", "categ": "VARIOS"},
                
            ]
        }

        report = ConsolidateTaking().get(my_taking.pk)
        assert(len(report) == spected_data["report"]["items_skus"])
        for item in spected_data["sample_products"]:
            assert (
                    item["total_onhand"] 
                    == 
                    sum([i["total_onhand"] for i in report if i["account_code"] == item["account_code"]])
            )

        # comprobamos lo que no existen
        for item in spected_data["dont_exist"]:
            assert (
                    0
                    == 
                    sum([i["total_onhand"] for i in report if i["account_code"] == item["account_code"]])
            )
    
    def test_two_categories(self):
        sap_migration = SapMigration.get(180)
        my_taking = Taking.objects.create(
            id_sap_migration=sap_migration,
            warenhouses=json.dumps(
                [
                    "ALMACEN 10 DE AGOSTO",
                    "CONSIGNACIONES PB PROVEEDORES",
                ]
            ),
            categories=json.dumps(["VARIOS", "ACCESORIOS"]),
            user_manager=UserModel().get("evillota"),
        )

        spected_data = {
            "report": {
                "items_skus": 60,
                "total_onhand": 10336,
            },
            "sample_products": [
                {
                    "account_code": "11012133910102010200",
                    "total_onhand": 530,
                    "taking": 0,
                    "pending": 530,
                    "is_complete": False,
                },{
                    "account_code": "07023312404303020000",
                    "total_onhand": 1,
                    "taking": 0,
                    "pending": 1,
                    "is_complete": False,
                },{
                    "account_code": "09015932401401010001",
                    "total_onhand": 1147,
                    "taking": 0,
                    "pending": 1147,
                    "is_complete": False,
                }
            ]
        }

        report = ConsolidateTaking().get(my_taking.pk)
        assert(len(report) == spected_data["report"]["items_skus"])
        for item in spected_data["sample_products"]:
            assert (
                    item["total_onhand"] 
                    == 
                    sum([i["total_onhand"] for i in report if i["account_code"] == item["account_code"]])
            )

    def test_taking_with_inputs(self):
        taking = Taking.get(88)
        report = ConsolidateTaking().get(taking.pk)

        spected_data = {
            "report": {
                "items_skus": 635,
                "total_onhand": 80715,
                "total_inputs": 80829,
            },
            "sample_products": [
                {
                    "account_code": "11012133910101010200",
                    "id_product": 3660,
                    "type_product": "VARIOS",
                    "product": "AGUA TONICA FEVER TREE GINGER INDIAN PREMIUM",
                    "ean_13_code": "5060108450003",
                    'quantity_per_box': 24,
                    "capacity": 200,
                    "total_onhand": 540,
                    "taking": 540,
                    "pending": 0,
                    "is_complete": True,
                },{
                    "account_code": "01012094410101030750",
                    "id_product": 1508,
                    "type_product": "LICORES",
                    "product": "VINO ESP. JUAN GIL ETIQUETA AMARILLA",
                    "ean_13_code": "8437005068001",
                    'quantity_per_box':12,
                    "capacity": 750,
                    "total_onhand": 68,
                    "taking": 182,
                    "pending": -114,
                    "is_complete": False,
                },{
                    "account_code": "02012130020202010750",
                    "id_product": 2094,
                    "type_product": "LICORES",
                    "product": "WHISKY SOMETHING SPECIAL",
                    "ean_13_code": "080432402795",
                    'quantity_per_box': 12,
                    "capacity": 750,
                    "total_onhand": 1876,
                    "taking": 1876,
                    "pending": 0,
                    "is_complete": True,
                }
            ]
        }

        report = ConsolidateTaking().get(taking.pk)
        assert(len(report) == spected_data["report"]["items_skus"])

        for item in spected_data['sample_products']:
            for itm_report in report:
                if itm_report['account_code'] == item['account_code']:
                    assert item == itm_report
                    break



        
       