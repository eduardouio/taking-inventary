from rest_framework.views import APIView
from rest_framework.response import Response
from api.Serializers import SapMigrationSerializer, CustomUserSerializer
from common.WizardMigrationData import WizardMigrationData


# /api/common/wizard-assistant/<int:id_sap_migration>/
class WizardAPIView(APIView):

    def get(self, request, id_sap_migration, *args, **kwargs):
        try:
            report = WizardMigrationData().get(id_sap_migration)
        except Exception as e:
            return Response({'detail': str(e)}, status=404)

        sap_migration = SapMigrationSerializer(report['sap_migration']).data
        all_users = CustomUserSerializer(report['all_users'], many=True).data

        wizard_data = {
            'sap_migration': sap_migration,
            'warenhouses': report['warenhouses'],
            'type_products': report['type_products'],
            'all_users': all_users,
        }

        return Response(wizard_data)
