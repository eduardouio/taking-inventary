import json

from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserManager

# /accounts/create/team/
class UpdateTeamCV(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        team_data = json.loads(request.POST.get('team'))
        team = Team.get(team_data['pk'])
        team.warenhouse_assistant = team_data['fields']['warenhouse_assistant']
        team.notes = team_data['fields']['notes']
        team.save()
        return HttpResponse()
    