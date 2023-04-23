import json

from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

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
            counter = self.verify_taking_data(
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
                notes=item["notes"]
            )
            report.append(my_taking)

        try:
            TakinDetail.objects.bulk_create(report)
        except Exception as e:
            return HttpResponse(
                "Error al registrar datos {}".format(e.__str__),
                status=400)

        return HttpResponse("Updated success", status=201)

    def verify_data_exist(self, taking_data, taking, team):
        items_not_found = []
        regitered_items = TakinDetail.objects.filter(
            id_taking_id=taking_data["taking"]["pk"]
        ).filter(
            id_team=taking_data["team"]["pk"]
        )

        for line in regitered_items:
            line_regitered = {
                "pk_product": line.account_code_id,
                "taking_total_boxes": line.taking_total_boxes,
                "taking_total_bottles": line.taking_total_bottles,
                "notes": line.notes,

            }
            for item in taking_data["report"]:
                line_report = {
                    "pk_product": item["pk"],
                    "taking_total_boxes": item["taking_total_boxes"],
                    "taking_total_bottles": item["taking_total_bottles"],
                    "notes": item["notes"],
                }
                if line_regitered['pk_product'] == line_report['pk_product']:
                    if line_regitered != line_report:
                        items_not_found.append(line_report)

        for item_new in items_not_found:
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
            )

        return len(items_not_found)
