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
    """
        Retorna el detalle para un producto, filtrado por bodegas
        las bodegas se obtienen del registro de toma
    """

    def get(self, request, id_migration, id_taking, id_product) -> JsonResponse:

        taking = Taking.get(id_taking)

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
            'account_code': id_product,
            'id_migration': id_migration,
            'query': json.loads(serialize('json', query)),
        }
        return JsonResponse(response_data)
