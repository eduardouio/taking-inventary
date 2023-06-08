from rest_framework.views import APIView
from rest_framework.response import Response
from recounts.lib import MakeRecount


# /api/common/recount/<int:id_taking>/<str:account_code>/
class RecountAPIView(APIView):
    def get(self, request, id_taking, account_code, format=None):
        account_code = account_code if account_code != 'all' else None

        recount = MakeRecount()
        status = recount.make(id_taking, account_code)

        if status:
            return Response({'status': 'ok'})

        return Response({'status': 'toma cerrada'})
