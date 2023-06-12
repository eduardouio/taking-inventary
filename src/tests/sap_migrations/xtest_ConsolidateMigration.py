import pytest
from sap_migrations.lib.ConsolidateMigration import ConsolidateMigration
from sap_migrations.models import SapMigration, SapMigrationDetail


@pytest.mark.django_db
class TestConsolidateMigration(object):

    def test_get(self, mocker):
        consolidate = ConsolidateMigration()
        report = consolidate.get(55)

        spected_data = {
            "by_company_name": [
                {
                    "company": "AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.",
                    "account_code": "02012130020202010750",
                    "name": "WHISKY SOMETHING SPECIAL",
                    "on_hand": 716,
                    "on_order": 878640,
                    "is_commited": 0,
                    "avaliable": 879356,
                }, {
                    "company": "CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.",
                    "account_code": "02012130020202010750",
                    "name": "WHISKY SOMETHING SPECIAL",
                    "on_hand": 2055,
                    "on_order": 0,
                    "is_commited": 15,
                    "avaliable": 2040,
                }, {
                    "company": "SERVMULTIMARC CIA. LTDA.",
                    "account_code": "02012130020202010750",
                    "name": "WHISKY SOMETHING SPECIAL",
                    "on_hand": 1774,
                    "on_order": 0,
                    "is_commited": 0,
                    "avaliable": 1774,
                }, {
                    "account_code": "02012130020202010750",
                    "name": "WHISKY SOMETHING SPECIAL",
                    "company": "VINOS Y ESPIRITUOSOS DEL LITORAL VINLITORAL S.A.",
                    "on_hand": 8370,
                    "on_order": 0.0,
                    "is_commited": 30,
                    "avaliable": 8340,
                }, {
                    "company": "VINOS Y ESPIRITUOSOS VINESA S.A",
                    "account_code": "02012130020202010750",
                    "name": "WHISKY SOMETHING SPECIAL",
                    "on_hand": 10757,
                    "on_order": 0,
                    "is_commited": 1524,
                    "avaliable": 9233,
                }
            ]
        }

        test_data = [
            i for i in report['by_company_name']
            if i['account_code'] == "02012130020202010750"
        ]
        assert test_data == spected_data['by_company_name']
