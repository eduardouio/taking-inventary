from rest_framework.views import APIView
from rest_framework.response import Response


class AllSAPMigrationData(APIView):

    def get(self, request, *args, **kwargs):
        """
        Retorna todos los datos necesarios para crear una toma de inventario

        Parameters:
            request (HttpRequest): La solicitud HTTP recibida.
            *args: Argumentos posicionales adicionales.
            **kwargs: Argumentos de palabras clave adicionales.

        Returns:
            Response: {
                "sap_migration": objeto de migracion,
                "warenhouses": bodegas de las migraciones,
                "enterprises": propietarios que tienen saldo en las bodegas,
                "sap_migration_warenhouses": bodegas de las migraciones,
                "all_users": todos los usuarios asistentes del sistema,
                "types_products": tipos de productos,
            }

        """

        sap_migrations = {
            "sap_migration": {},
            "warenhouses": [],
            "enterprises": {},
            "sap_migration_warenhouses": [],
            "all_users": [],
            "types_products": [],
        }
        return Response({
            "status": "OK",
            "message": "AllSAPMigrationData"
        })
