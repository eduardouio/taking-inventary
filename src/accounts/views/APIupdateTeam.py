import json
from django.http import HttpResponse
from django.views.generic import View

from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserModel

# para test
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# /accounts/update-team/
@method_decorator(csrf_exempt, name="dispatch")
class APIupdateTeam(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        team = Team.objects.get(id_team=data["team"]["pk"])
        team.warenhouse_assistant = data["team"]["fields"]["warenhouse_assistant"]
        team.notes = data["team"]["fields"]["notes"]
        team.save()
        return HttpResponse("ok", status=200)
