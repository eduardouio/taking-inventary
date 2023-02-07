import json

from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize

from takings.models import TakinDetail
from products.models import Product


# /takings/api/taking-detail/taking/<int:id_taking>/product/<str:account_code>/
class APITakingDetail(View):

    def get(self, request, id_taking, id_product):
        my_product = Product.get(account_code=id_product)
        details = TakinDetail.objects.filter(
            id_taking=id_taking
        ).filter(account_code=my_product)

        response_data = {
            'id_product': id_product,
            'id_taking': id_taking,
            'product': json.loads(serialize('json', [my_product]))[0],
            'query': json.loads(serialize('json', details)),
        }

        return JsonResponse(response_data)
