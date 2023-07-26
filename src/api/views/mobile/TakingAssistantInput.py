import json

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models.Team import Team
from api.Serializers import (CustomUserSerializer, ProductSerializer,
                             TakingSerializer, TeamSerializer)
from products.models import Product
from sap_migrations.models import SapMigrationDetail
from takings.models import Taking


# api/mobile/assistant/id_tk/<int:id_taking>/id_tm/<int:id_team>/
# name='api-assistant-input'
class TakingAssistantInput(APIView):

    def get(self, request, id_taking, id_team, *args, **kwargs):
        taking = get_object_or_404(Taking, pk=id_taking)
        team = get_object_or_404(Team, pk=id_team)

        return Response({
            'taking': TakingSerializer(taking).data,
            'team': TeamSerializer(team).data,
            'user': CustomUserSerializer(team.manager).data,
            'products': self.get_products(taking),
        }, status=status.HTTP_200_OK)

    def get_products(self, taking):
        products = []
        warenhouses = json.loads(taking.warenhouses)
        # primero recuperamos los productos por bodega de la migracion
        for warenhouse in warenhouses:
            whrs_products = SapMigrationDetail.objects.filter(
                id_sap_migration=taking.id_sap_migration,
                warenhouse_name=warenhouse
            ).values_list('account_code', flat=True).distinct()
            # solo insertamos los codigos nuevos
            [products.append(i) for i in whrs_products if i not in products]

        return [ProductSerializer(Product.get(x)).data for x in products]
