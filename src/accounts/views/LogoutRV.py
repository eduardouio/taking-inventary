from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


# /accounts/logout/
class LogoutRV(RedirectView):
    url = '/'
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(self.get_redirect_url())