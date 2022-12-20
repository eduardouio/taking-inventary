from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from accounts.models.Team import Team
from accounts.forms import UserForm
from accounts.mixins import ValidateAssistantMixin
from takings.models import Taking


# /mobile/dashboard/
class DashboarTV(ValidateAssistantMixin, TemplateView):
    template_name = 'mobile/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user_teams = Team.get_teams_by_user(request.user)
        user_takings = []
        for team in user_teams:
            taking = Taking.get_by_team(team.pk)
            if taking:
                user_takings.append(taking)
        user_form = UserForm(instance=request.user)
        page_data = {
            'title_page': 'Dashboar Toma',
            'takings': user_takings,
            'user_form': user_form, 
        }

        return self.render_to_response({**context, **page_data})
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        user_form.save()
        return HttpResponseRedirect('/mobile/dashboard/')
