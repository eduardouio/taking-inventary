from rest_framework.response import Response
from rest_framework.views import APIView

from api.Serializers import (CustomUserSerializer,
                             SapMigrationDetailSerializer,
                             SapMigrationSerializer)
from sap_migrations.lib import LoadMigration
from accounts.models.CustomUserModel import CustomUserModel
from sap_migrations.models import SapMigrationDetail, SapMigration


# /api/migrations/all-data/
class AllSAPMigrationData(APIView):

    def get(self, request, *args, **kwargs):
        """
        Retorna todos los datos necesarios para crear una toma de inventario
        """
        # generamos una nueva migracion
        sap_migration = LoadMigration().load()
        sap_migration_detail = SapMigrationDetail.objects.filter(
            id_sap_migration=sap_migration
        )

        report = {
            "migration": SapMigrationSerializer(sap_migration).data,
            "migration_detail": SapMigrationDetailSerializer(sap_migration_detail, many=True).data,

        }
        return Response({
            "report": report
        })
