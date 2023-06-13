from rest_framework.views import APIView
from rest_framework.response import Response
from sap_migrations.models import SapMigration
from api.Serializers import SapMigrationSerializer


# /api/common/taking-wizard/
class WizardAPIView(APIView):

    def get(self, request, id_sap_migration, *args, **kwargs):
        sap_migration = SapMigration.objects.get(pk=id_sap_migration)

        wizard_data = {
            'sap_migration': SapMigrationSerializer(sap_migration).data,
            'warenhouses': [],
            'type_products': [],
            'all_users': [],
        }

        return Response(wizard_data)
