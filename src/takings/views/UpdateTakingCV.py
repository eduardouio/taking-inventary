import json

from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from datetime import date

# para test
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from takings.models import Taking, TakinDetail
from accounts.models.Team import Team
from products.models import Product


# /takings/add-report/
@method_decorator(csrf_exempt, name="dispatch")
class UpdateTakingCV(CreateView):

    def post(self, request, *args, **kwargs):
        taking_data = json.loads(request.body)
        taking = get_object_or_404(
            Taking,
            pk=taking_data["taking"]["pk"]
        )

        if not taking.is_active:
            return HttpResponse("Inventario Cerrado", status=400)

        team = Team.objects.get(id_team=taking_data["team"]["pk"])

        if TakinDetail.token_exist(team.token_team):
            counter = self.verify_data_exist(
                taking_data,
                taking,
                team
            )
            return HttpResponse(
                "Datos ya registrados, {} registros creados".format(counter),
                status=400
            )
        products = Product.objects.filter(pk__in=[
            item["product"]["pk"] for item in taking_data["report"]
        ])

        report = []

        for item in taking_data["report"]:
            product = [
                prod for prod in products if prod.pk == item["product"]["pk"]
            ][0]
            my_date_expiry = item["date_expiry"] if item["date_expiry"] != "" else None
            if my_date_expiry:
                my_date_expiry = date(
                    int(item["date_expiry"].split("-")[0]),
                    int(item["date_expiry"].split("-")[1]),
                    int(item["date_expiry"].split("-")[2])
                )
            my_year = item["year"] if item["year"] != "" else None
            if my_year:
                my_year = int(item["year"])

            my_taking = TakinDetail(
                id_taking=taking,
                account_code=product,
                id_team=team,
                token_team=team.token_team,
                taking_total_boxes=item["taking_total_boxes"],
                taking_total_bottles=item["taking_total_bottles"],
                quantity=(
                    item["taking_total_boxes"] * product.quantity_per_box
                ) + item["taking_total_bottles"],
                notes=item["notes"],
                year=my_year,
                date_expiry=my_date_expiry
            )
            report.append(my_taking)

        try:
            TakinDetail.objects.bulk_create(report)
        except Exception as e:
            return HttpResponse(
                "Error al registrar datos {}".format(e.__str__()),
                status=400)

        return HttpResponse("Updated success", status=201)

    def verify_data_exist(self, taking_data, taking, team):
        regitered_items = TakinDetail.objects.filter(
            id_taking_id=taking_data["taking"]["pk"]
        ).filter(
            id_team=taking_data["team"]["pk"]
        )

        details_db = []

        for line in regitered_items:
            my_date_expiry = line.date_expiry if line.date_expiry != "" else None
            if my_date_expiry:
                my_date_expiry = my_date_expiry.strftime("%Y-%m-%d")

            details_db.append(
                {
                    "pk_product": line.account_code_id,
                    "taking_total_boxes": line.taking_total_boxes,
                    "taking_total_bottles": line.taking_total_bottles,
                    "year": line.year,
                    "date_expiry": my_date_expiry,
                    "notes": line.notes,
                }
            )

        details_request = []
        for line in taking_data["report"]:
            details_request.append(
                {
                    "pk_product": line["pk"],
                    "taking_total_boxes": line["taking_total_boxes"],
                    "taking_total_bottles": line["taking_total_bottles"],
                    "year": line["year"] if line["year"] != "" else None,
                    "date_expiry": line["date_expiry"] if line["date_expiry"] != "" else None,
                    "notes": line["notes"],
                })

        items_not_found = [
            item for item in details_request if item not in details_db
        ]

        for item_new in items_not_found:
            my_date_expiry = item_new["date_expiry"] if item_new["date_expiry"] != "" else None
            if my_date_expiry:
                my_date_expiry = date(
                    int(item_new["date_expiry"].split("-")[0]),
                    int(item_new["date_expiry"].split("-")[1]),
                    int(item_new["date_expiry"].split("-")[2])
                )
            my_year = item_new["year"] if item_new["year"] != "" else None
            if my_year:
                my_year = int(item_new["year"])

            product = Product.objects.get(pk=item_new["pk_product"])
            TakinDetail.objects.create(
                id_taking=taking,
                account_code=product,
                id_team=team,
                token_team=team.token_team,
                taking_total_boxes=item_new["taking_total_boxes"],
                taking_total_bottles=item_new["taking_total_bottles"],
                quantity=(
                    item_new["taking_total_boxes"] * product.quantity_per_box
                ) + item_new["taking_total_bottles"],
                notes=item_new["notes"],
                year=my_year,
                date_expiry=my_date_expiry
            )

        return len(items_not_found)
