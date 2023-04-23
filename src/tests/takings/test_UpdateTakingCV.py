import json

# Dependencies:
# pip install pytest-mock
import pytest
from django.core.serializers import serialize
from django.test import RequestFactory
from accounts.models.Team import Team
from takings.models import TakinDetail, Taking
from takings.views.UpdateTakingCV import UpdateTakingCV


def request_data_factory():
    taking = Taking.get(32)
    team = Team.get(102)
    request_data = {
        "report": [
            {"pk": 3668, "taking_total_bottles": 8, "taking_total_boxes": 0,
                "notes": None, "year": None, "date_expiry": None},
            {"pk": 2425, "taking_total_bottles": 4, "taking_total_boxes": 0,
                "notes": None, "year": None, "date_expiry": None},
            {"pk": 681, "taking_total_bottles": 5, "taking_total_boxes": 0,
                "notes": None, "year": None, "date_expiry": None},
            {"pk": 2023, "taking_total_bottles": 13, "taking_total_boxes": 0,
                "notes": None, "year": None, "date_expiry": None},
        ],
        "taking": json.loads(serialize("json", [taking]))[0],
        "team": json.loads(serialize("json", [team]))[0],
    }

    return {
        "team": team,
        "taking": taking,
        "request_data": request_data,
    }


@pytest.mark.django_db
class TestUpdateTakingCV:
    def test_verify_data_exist_all_seted(self):
        request_data = request_data_factory()

        UpdateTaking = UpdateTakingCV()
        result = UpdateTaking.verify_data_exist(
            request_data["request_data"],
            request_data["taking"],
            request_data["team"]
        )
        regitered_items = TakinDetail.objects.filter(
            id_taking_id=request_data["taking"].pk
        ).filter(
            id_team=request_data["team"].pk
        )

        assert regitered_items.count() == 557
        assert result == 0

    def test_verify_data_exist_parted_exists(self):
        self.taking = Taking.get(32)
        self.team = Team.get(102)
        request_data = {
            "report": [
                {"pk": 3668, "taking_total_bottles": 8, "taking_total_boxes": 1,
                    "notes": None, "year": None, "date_expiry": None},
                {"pk": 2425, "taking_total_bottles": 4, "taking_total_boxes": 1,
                    "notes": None, "year": None, "date_expiry": None},
                {"pk": 681, "taking_total_bottles": 5, "taking_total_boxes": 0,
                    "notes": None, "year": None, "date_expiry": None},
                {"pk": 2023, "taking_total_bottles": 13, "taking_total_boxes": 0,
                    "notes": None, "year": None, "date_expiry": None},
            ],
            "taking": json.loads(serialize("json", [self.taking]))[0],
            "team": json.loads(serialize("json", [self.team]))[0],
        }

        UpdateTaking = UpdateTakingCV()
        result = UpdateTaking.verify_data_exist(
            request_data,
            self.taking,
            self.team
        )
        regitered_items = TakinDetail.objects.filter(
            id_taking_id=self.taking.pk
        ).filter(
            id_team=self.team.pk
        )

        assert regitered_items.count() == 559
        assert result == 2

    def test_report_for_new_taking(self, mocker):

        # Setup
        self.taking = Taking.get(88)
        self.team = Team.get(102)
        taking_details_before = TakinDetail.objects.filter(
            id_taking=self.taking
        ).count()
        # Mock Products
        my_products = [
            [
                {"pk": 3668, "name": "Product 1", "code": "1234567890123", }
            ], [
                {"pk": 2425, "name": "Product 2", "code": "1234567890124", }
            ], [
                {"pk": 681, "name": "Product 3", "code": "1234567890125", }
            ], [
                {"pk": 2023, "name": "Product 4", "code": "1234567890126", }
            ]
        ]

        request_data = {
            "report": [
                {"pk": 3668, "taking_total_bottles": 8, "year": None, "date_expiry": None,
                    "taking_total_boxes": 0, "notes": None, "product": my_products[0][0]},
                {"pk": 2425, "taking_total_bottles": 4, "year": None, "date_expiry": None,
                    "taking_total_boxes": 0, "notes": None, "product": my_products[1][0]},
                {"pk": 681, "taking_total_bottles": 5, "year": None, "date_expiry": None,
                    "taking_total_boxes": 0, "notes": None, "product": my_products[2][0]},
                {"pk": 2023, "taking_total_bottles": 13, "year": None, "date_expiry": None,
                    "taking_total_boxes": 0, "notes": None, "product": my_products[3][0]},
            ],
            "taking": json.loads(serialize("json", [self.taking]))[0],
            "team": json.loads(serialize("json", [self.team]))[0],
        }

        # Exercise
        view = UpdateTakingCV.as_view()
        request_factory = RequestFactory()
        request = request_factory.post(
            "/takings/add-report/",
            json.dumps(request_data),
            content_type="application/json"
        )
        response = view(request)
        # Verify
        taking_details_after = TakinDetail.objects.filter(
            id_taking=self.taking
        ).count()

        assert response.status_code == 201
        assert (taking_details_after - taking_details_before) == 4

    def test_taking_is_closed(self):
        self.taking = Taking.get(32)
        self.team = Team.get(102)
        request_data = {
            "report": [

                {"pk": 3668, "taking_total_bottles": 8,
                    "taking_total_boxes": 0, "notes": None, "year": None, "date_expiry": None, },
                {"pk": 2425, "taking_total_bottles": 4,
                    "taking_total_boxes": 0, "notes": None, "year": None, "date_expiry": None, },
                {"pk": 681, "taking_total_bottles": 5,
                    "taking_total_boxes": 0, "notes": None, "year": None, "date_expiry": None, },
                {"pk": 2023, "taking_total_bottles": 13,
                    "taking_total_boxes": 0, "notes": None, "year": None, "date_expiry": None, },
            ],
            "taking": json.loads(serialize("json", [self.taking]))[0],
            "team": json.loads(serialize("json", [self.team]))[0],
        }

        # Exercise
        view = UpdateTakingCV.as_view()
        request_factory = RequestFactory()
        request = request_factory.post(
            "/takings/add-report/",
            json.dumps(request_data),
            content_type="application/json"
        )
        response = view(request)

        # Verify
        assert response.status_code == 400

    def error_404_response_method(self):
        request_data = {
            "taking": {
                "pk": 9999999
            }
        }
        view = UpdateTakingCV.as_view()
        request_factory = RequestFactory()
        request = request_factory.post(
            '/takings/add-report/',
            json.dumps(request_data),
            content_type="application/json"
        )
        response = view(request)
        assert response.status_code == 404
