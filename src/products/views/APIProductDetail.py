import json
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize

from products.models import Product
from sap_migrations.models import SapMigrationDetail


# /products/api/detail/product/<int:pk>/migration/<int:pk>/
class APIProductDetail(View):

    def get(self, request, id_product, id_migration):
        my_product = Product.get(account_code=id_product)
        query = SapMigrationDetail.objects.filter(
            account_code=my_product.account_code,
            id_sap_migration_id=id_migration
        )
        response_data = {
            'id_product': id_product,
            'id_migration': id_migration,
            'product': json.loads(serialize('json', [my_product])),
            'query': json.loads(serialize('json', query)),
        }
        return JsonResponse(response_data)
