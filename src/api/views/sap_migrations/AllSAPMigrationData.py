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
        # cargamos los datos de la migracion
        # sap_migration = LoadMigration().load()
        # sap_migration_detail = SapMigrationDetail.objects.filter(
        #    id_sap_migration=sap_migration
        # )

        # para probar api
        sap_migration = SapMigration.objects.get(pk=1)
        sap_migration_detail = SapMigrationDetail.objects.filter(
            id_sap_migration=sap_migration
        )[:2000]

        # lista de usuarios asistentes
        all_assistant_users = CustomUserModel.objects.filter(role='asistente')

        report = {
            "migration": SapMigrationSerializer(sap_migration).data,
            "migration_detail": SapMigrationDetailSerializer(sap_migration_detail, many=True).data,
            "all_assistant_user": CustomUserSerializer(all_assistant_users, many=True).data

        }
        return Response({
            "report": report
        })
