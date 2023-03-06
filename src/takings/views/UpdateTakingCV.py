import json

from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from takings.models import Taking, TakinDetail
from accounts.models.Team import Team
from products.models import Product


# /takings/add/report/
class UpdateTakingCV(LoginRequiredMixin, CreateView):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('data'))
        report_data = data['report']
        taking = Taking.get(data['taking']['pk'])

        if taking is None:
            return HttpResponse('No Existe', status=404)

        if not taking.is_active:
            return HttpResponse('Inventario Cerrado', status=400)

        team = Team.objects.get(id_team=data['team']['pk'])

        if TakinDetail.token_exist(team.token_team):
            return HttpResponse('Datos ya registrados', status=400)

        try:
            report = []

            for item in report_data:
                product = Product.objects.get(
                    account_code=item['product']['fields']['account_code'])

                my_taking = TakinDetail(
                    id_taking=taking,
                    account_code=product,
                    id_team=team,
                    token_team=team.token_team,
                    taking_total_boxes=item['taking_total_boxes'],
                    taking_total_bottles=item['taking_total_bottles'],
                    quantity=(item['taking_total_boxes'] *
                              product.quantity_per_box) + item['taking_total_bottles'],
                    notes=item['notes']
                )
                report.append(my_taking)

            TakinDetail.objects.bulk_create(report)

            return HttpResponse('Updated success', status=201)

        except Exception as e:
            return HttpResponse(str(e), status=500)
