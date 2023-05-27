# consolidate takinf and taking detail info
# get user manager
# ger teams whit user manager team

from django.http import Http404
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

from api.Serializers import (CustomUserSerializer, ProductSerializer,
                             TakingSerializer, TeamSerializer)
from takings.lib import ConsolidateTaking
from takings.models import Taking
from accounts.models.CustomUserModel import CustomUserModel


# /api/all-taking-data/<id_taking>/
class AllTakingDataAPIView(APIView):

    def get(self, request, id_taking, *args, **kwargs):
        taking = Taking.get(id_taking)
        if taking is None:
            raise Http404

        detail = ConsolidateTaking().get(id_taking)
        report = []
        for item in detail["report"]:
            product = ProductSerializer(item["product"]).data
            report.append({
                "product": product,
                "sap_stock": item["sap_stock"],
                "is_complete": item["is_complete"],
                "tk_bottles": item["tk_bottles"],
                "tk_boxes": item["tk_boxes"],
                "tk_quantity": item["tk_quantity"],
            })

        teams = TeamSerializer(taking.teams.all(), many=True).data
        teams = [dict(t) for t in teams]
        teams_activity = self.teams_activity(id_taking)
        for team in teams:
            manager = CustomUserModel.objects.get(pk=team["manager"])
            team["manager"] = CustomUserSerializer(manager).data
            team["activity"] = {
                'id_team_id': team["id_team"],
                'count': 0,
            }
            for activity in teams_activity:
                if team["id_team"] == activity["id_team_id"]:
                    team["activity"] = activity

        data = {
            "taking": TakingSerializer(taking).data,
            "teams": teams,
            "enterprises": detail["enterprises"],
            "report": report,
            "manager": CustomUserSerializer(taking.user_manager).data,
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
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
