from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from api.Serializers import TeamSerializer
from accounts.models.Team import Team


# /api/teams/update-team/<id_team>/
class UpdateTeamAPIView(UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id_team'

    def put(self, requests, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=requests.data)
        is_valid = serializer.is_valid()
        if is_valid:
            self.perform_update(serializer)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
