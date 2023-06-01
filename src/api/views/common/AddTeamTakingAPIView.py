# agregamos un usuario a la toma

from rest_framework.views import APIView
from rest_framework.response import Response

from api.Serializers import TeamSerializer
from takings.models import Taking
from accounts.models.CustomUserModel import CustomUserModel
from accounts.models.Team import Team


# /api/common/add-team-taking/<id_taking>/
class AddTeamTakingAPIView(APIView):

    def post(self, request, id_taking, *args, **kwarg):
        taking = Taking.objects.get(id_taking=id_taking)
        for team in request.data['teams']:
            manager = CustomUserModel.objects.get(pk=team['id'])
            taking_teams = taking.teams.all()
            team = Team.objects.create(
                id_taking=taking.pk,
                group_number=len(taking_teams) + 1,
                manager=manager
            )
            team.save()
            taking.teams.add(team)
            taking.save()

        all_teams = TeamSerializer(taking.teams.all(), many=True).data
        all_teams = [dict(t) for t in all_teams]
        return Response(all_teams)
