
from django.contrib.auth.views import LoginView

class Login(LoginView):
    success_url = '/'
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        import ipdb;ipdb.set_trace()