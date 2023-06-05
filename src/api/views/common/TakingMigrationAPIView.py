# Retorna el detalle de la toma de un producto
# y el detalle del stock sap

import json

from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from api.Serializers import (CustomUserSerializer,
                             SapMigrationDetailSerializer,
                             TakingDetailSerializer, TeamSerializer)
from products.models import Product
from sap_migrations.models import SapMigrationDetail
from takings.models import TakinDetail, Taking


# /api/common/taking-migration/taking/<int:id_taking>/product/<str:account_code>/
class TakingMigrationAPIView(APIView):

    def get(self, request, id_taking, account_code):
        product = Product.get(account_code)

        # si el prodcuto no existe retorna un error
        if not product:
            return Response({"error": "Product not found"}, status=404)

        taking = Taking.get(id_taking)

        # si la toma no existe retorna un error
        if not taking:
            return Response({"error": "Taking not found"}, status=404)

        # obtemos el detalle de saldo en las bodegas de las tomas
        custom_filters = []
        for warenhouse in json.loads(taking.warenhouses):
            custom_filters.append(warenhouse)

        filters = Q()
        for filter in custom_filters:
            filters |= Q(warenhouse_name=filter)

        migration_detail = SapMigrationDetail.objects.filter(
            id_sap_migration_id=taking.id_sap_migration_id
        ).filter(
            account_code=product.account_code
        ).filter(filters)

        # obtemos el detalle de la toma
        taking_detail = TakinDetail.objects.filter(
            id_taking=id_taking
        ).filter(account_code_id=product.pk)

        # serializamos los datos
        takings_report = []
        for item in taking_detail:
            itm_serializer = TakingDetailSerializer(item)
            team_serializer = TeamSerializer(item.id_team)
            user_serializer = CustomUserSerializer(item.id_team.manager)
            takings_report.append({
                "taking": itm_serializer.data,
                "team": team_serializer.data,
                "user": user_serializer.data,
            })

        migration_detail = [
            dict(item)
            for item
            in SapMigrationDetailSerializer(migration_detail, many=True).data
        ]

        # datos a retornar
        detail_data = {
            "migrations": migration_detail,
            "takings": takings_report,
        }

        return Response(detail_data, status=200)
