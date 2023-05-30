from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from api.Serializers import TakingSerializer
from takings.models import Taking


# /api/takings/update-taking/
class UpdateTakingAPIView(UpdateAPIView):
    queryset = Taking.objects.all()
    serializer_class = TakingSerializer
    lookup_field = 'id_taking'

    def put(self, requests, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=requests.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
