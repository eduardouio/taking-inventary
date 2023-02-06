import json

from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize

from products.models import Product
from sap_migrations.models import SapMigrationDetail
from takings.models import Taking


# /sap/api/migration/<int:id_migration>/taking/<str:id_taking>/product/<int:id_product>/
class APISapMigrationDetail(View):

    def get(self, request, id_migration, id_taking, id_product,):

        taking = Taking.get(id_taking)

        my_product = Product.get(account_code=id_product)
        custom_filters = []
        for warenhouse in json.loads(taking.warenhouses):
            custom_filters.append(warenhouse)

        filters = Q()
        for filter in custom_filters:
            filters |= Q(warenhouse_name=filter)

        query = SapMigrationDetail.objects.filter(
            id_sap_migration_id=id_migration
        ).filter(
            account_code=id_product
        ).filter(filters)

        response_data = {
            'id_product': id_product,
            'id_migration': id_migration,
            'product': json.loads(serialize('json', [my_product]))[0],
            'query': json.loads(serialize('json', query)),
        }
        return JsonResponse(response_data)
