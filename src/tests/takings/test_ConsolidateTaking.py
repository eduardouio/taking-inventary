import json

import pytest

from takings.lib import ConsolidateTaking
from takings.models import Taking
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
                "items_skus": 536,
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
        assert( len(report) == spected_data["report"]["items_skus"] )

