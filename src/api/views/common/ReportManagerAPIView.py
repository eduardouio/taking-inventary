from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from api.Serializers import TakingDetailSerializer, ProductSerializer

from takings.models import TakinDetail


class ReportManagerAPIView(APIView):

    def get(self, *args, **kwargs):
        report = []
        
        if kwargs['type_report'] == 'years':
            details = TakinDetail.objects.filter(
                id_taking_id = kwargs['id_taking'],
                year__isnull = False
            )

            for detail in details:
                item = TakingDetailSerializer(detail).data
                product = ProductSerializer(detail.account_code).data
                item['product'] = product
                report.append(item)
        
        if kwargs['type_report'] == 'endDate':
            details = TakinDetail.objects.filter(
                id_taking_id = kwargs['id_taking'],
                date_expiry__isnull = False
            )

            for detail in details:
                item = TakingDetailSerializer(detail).data
                product = ProductSerializer(detail.account_code).data
                item['product'] = product
                report.append(item)
        
        if report:
            return Response(report, status=HTTP_200_OK)
        
        return Response({}, status=HTTP_400_BAD_REQUEST)
