from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from api.Serializers import TakingSerializer
from takings.models import Taking
from datetime import datetime


# /api/takings/update-taking/<id_taking>/
class UpdateTakingAPIView(UpdateAPIView):
    queryset = Taking.objects.all()
    serializer_class = TakingSerializer
    lookup_field = 'id_taking'

    def put(self, requests, *args, **kwargs):
        instance = self.get_object()
        # alimentamos los campos de fecha y hora de cierre
        if requests.data.get('date_end_taking'):
            requests.data['date_end_taking'] = datetime.now()
            requests.data['hour_end'] = datetime.now().time()

        serializer = self.get_serializer(instance, data=requests.data)
        is_valid = serializer.is_valid()
        if is_valid:
            self.perform_update(serializer)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
