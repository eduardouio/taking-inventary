from rest_framework.views import APIView
from rest_framework.response import Response
from recounts.lib import MakeRecount


# /api/common/recount/<int:id_taking>/<str:account_code>/
class RecountAPIView(APIView):
    """ Elimna las tomas de inventario que no esten cerradas
        elimnar todas las tomas de inventario que no esten cerradas

        /api/common/recount/<int:id_taking>/all/

        eliminar las tomas de un item
        /api/common/recount/<int:id_taking>/<str:account_code>/
    """

    def get(self, request, id_taking, account_code, format=None):
        account_code = account_code if account_code != 'all' else None

        recount = MakeRecount()
        status = recount.make(id_taking, account_code)

        if status:
            return Response({'status': 'ok'})

        return Response({'status': 'toma cerrada'})
