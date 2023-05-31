from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.Serializers import TeamSerializer
from accounts.models.Team import Team


# /api/teams/create-team/
class CreateTeamAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        is_valid = serializer.is_valid()
        if is_valid:
            self.perform_create(serializer)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
