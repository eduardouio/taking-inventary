# consolidate takinf and taking detail info
# get user manager
# ger teams whit user manager team

from rest_framework.views import APIView
from api.Serializers import TakingSerializer, TakingDetailSerializer
from takings.models import Taking, TakingDetail


# /api/all-taking-data/<id_taking>/
class AllTakingData(APIView):

    def get(self, request, id_taking, *args, **kwargs):
        taking = Taking.objects.get(id=id_taking)
        taking_detail = TakingDetail.objects.filter(taking=taking)
        taking_serializer = TakingSerializer(taking)
        taking_detail_serializer = TakingDetailSerializer(
            taking_detail, many=True)
        view_data = {
            "taking": taking_serializer.data,
            "taking_detail": taking_detail_serializer.data
        }
        return Response(view_data, status=200, safe=False)
