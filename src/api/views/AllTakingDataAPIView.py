# consolidate takinf and taking detail info
# get user manager
# ger teams whit user manager team

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from api.Serializers import TakingSerializer, TeamSerializer, SapMigrationDetailSerializer, ProductSerializer
from takings.models import Taking
from takings.lib import ConsolidateTaking
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


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

        teams = taking.teams.all()

        data = {
            "taking": TakingSerializer(taking).data,
            "teams": TeamSerializer(teams, many=True).data,
            "report": report,
            "enterprises": detail["enterprises"]
        }

        return Response(data)
