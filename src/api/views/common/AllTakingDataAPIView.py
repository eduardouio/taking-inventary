# consolidate takinf and taking detail info
# get user manager
# ger teams whit user manager team

import json

from django.db import connection
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models.CustomUserModel import CustomUserModel
from api.Serializers import (CustomUserSerializer, ProductSerializer,
                             TakingSerializer, TeamSerializer, RecountTakingsSerializer)
from products.models import Product
from takings.lib import ConsolidateTaking
from takings.models import TakinDetail, Taking
from sap_migrations.models import SapMigrationDetail
from recounts.models import RecountTakings



# /api/common/taking-data/<id_taking>/
class AllTakingDataAPIView(APIView):

    def get(self, request, id_taking, *args, **kwargs):
        taking = Taking.get(id_taking)
        if taking is None:
            raise Http404

        # recuperamos reporte consolidado
        detail = ConsolidateTaking().get(id_taking)
        report = []

        # personalizamos reporte
        for item in detail:
            product = ProductSerializer(Product.get(item['account_code'])).data
            report.append({
                "product": product,
                "sap_stock": item["total_onhand"],
                "is_complete": item["is_complete"],
                "tk_quantity": item["taking"],
            })

        # recuperamos equipos y creamos el diccionario
        teams = TeamSerializer(taking.teams.all(), many=True).data
        teams = [dict(t) for t in teams]

        teams_activity = self.teams_activity(id_taking)

        for team in teams:
            manager = CustomUserModel.objects.get(pk=team["manager"])
            team["manager"] = CustomUserSerializer(manager).data
            team["selected"] = True
            team["activity"] = {
                'id_team_id': team["id_team"],
                'count': 0,
            }
            for activity in teams_activity:
                if team["id_team"] == activity["id_team_id"]:
                    team["activity"] = activity
        # obtenemos todas las bodegas de la migracion
        all_warenhouses = self.get_all_warenhouses(taking)

        # obtenemos todos los usuarios asistentes
        all_users_assistants = CustomUserModel.objects.filter(
            role='asistente'
        )

        # serializamos el objeto
        all_users_assistants = CustomUserSerializer(
            all_users_assistants, many=True
        ).data

        # creamos el diccionario
        all_users_assistants = [dict(t) for t in all_users_assistants]

        # agregamos campo selected
        for user in all_users_assistants:
            user["selected"] = False
        
        # enterprises
        enterprises = SapMigrationDetail.objects.filter(
            id_sap_migration = taking.id_sap_migration,
        ).filter(   
            warenhouse_name__in=json.loads(taking.warenhouses)
        ).values('company_name').order_by('company_name').distinct()

        # reconteos
        recounts = RecountTakings.objects.filter(id_taking = taking)

        data = {
            "taking": TakingSerializer(taking).data,
            "teams": teams,
            "enterprises": [e['company_name'] for e in enterprises],
            "report": report,
            "manager": CustomUserSerializer(taking.user_manager).data,
            "all_warenhouses": all_warenhouses,
            "all_users_assistants": all_users_assistants,
            "recounts": RecountTakingsSerializer(recounts, many=True).data,
        }

        return Response(data)

    def teams_activity(self, id_taking):
        query = """
            SELECT td.id_team_id, COUNT(DISTINCT(td.token_team)) 
            FROM takings_takindetail td where td.id_taking_id = {} 
            GROUP BY td.id_team_id;
        """.format(id_taking)
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for item in data:
            # ultima toma de equipo
            # Obtener el último TakingDetail para un id_team específico ordenado por created desc
            last_taking = TakinDetail.objects.filter(id_team_id=430).order_by(
                '-created'
            ).first()
            item["last_taking"] = last_taking.created

        return data

    def get_all_warenhouses(self, taking):
        query = """
            SELECT DISTINCT(smd.warenhouse_name) 
            FROM sap_migrations_sapmigrationdetail smd
            WHERE smd.id_sap_migration_id = {};
        """.format(taking.id_sap_migration.pk)
        cursor = connection.cursor()
        cursor.execute(query)
        used_warenhouses = json.loads(taking.warenhouses)

        data = [{"name": list(row)[0],
                 "selected": False
                 }
                for row in cursor.fetchall() if list(row)[0] not in used_warenhouses
                ]

        used_warenhouses = [{"name": w, "selected": True} for w in used_warenhouses]
        data = used_warenhouses + data
        return data
