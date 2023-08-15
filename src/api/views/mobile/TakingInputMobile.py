from takings.models import Taking
from rest_framework.views import APIView

class TakingInputMobile(APIView):
    """ Recibe las tomas enviadas por la SPA Mobil """
    def post(self, request, *args, **kwargs):
        pass