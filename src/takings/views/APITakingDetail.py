import json

from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize

from takings.models import TakinDetail
from products.models import Product
from accounts.models.Team import Team


# /takings/api/taking-detail/taking/<int:id_taking>/product/<str:account_code>/
class APITakingDetail(View):

    def get(self, request, id_taking, id_product):
        my_product = Product.get(account_code=id_product)
        details = TakinDetail.objects.filter(
            id_taking=id_taking
        ).filter(account_code=my_product)

        report = []


        for item in details:
            report.append({
                'detail': json.loads(serialize('json', [item]))[0],
                'team':  {
                    'manager': '{} {}'.format(
                                        item.id_team.manager.first_name,
                                        item.id_team.manager.last_name),
                    'assistant': item.id_team.warenhouse_assistant,
                    'username': item.id_team.manager.username,
                },
            })

        #import ipdb;ipdb.set_trace()
        response_data = {
            'id_product': id_product,
            'id_taking': id_taking,
            'product': json.loads(serialize('json', [my_product]))[0],
            'query': report,
        }

        return JsonResponse(response_data)
