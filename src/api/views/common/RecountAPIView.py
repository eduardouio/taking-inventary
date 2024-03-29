from rest_framework.views import APIView
from rest_framework.response import Response
from recounts.lib import MakeRecount


# /api/common/recount/<int:id_taking>/<str:account_code>/
class RecountAPIView(APIView):
    """Elimina las tomas de inventario que no estén cerradas.

    Args:
        id_taking (int): ID de la toma de inventario.
        account_code (str): Código contable del producto a eliminar.

    API endpoints:
        /api/common/recount/<int:id_taking>/all/
            Eliminar las tomas de un item.

        /api/common/recount/<int:id_taking>/<str:account_code>/
            Eliminar las tomas de inventario específicas para un producto.
    """

    def get(self, request, id_taking, account_code, format=None):
        account_code = account_code if account_code != 'all' else None

        recount = MakeRecount()
        status = recount.make(id_taking, account_code)

        if status:
            return Response({'status': 'ok'})

        return Response(
            {'status': 'No fue posible hacer el reconteo solicitado'}
        )
