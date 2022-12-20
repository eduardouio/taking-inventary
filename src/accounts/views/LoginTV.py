from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from accounts.models.CustomUserModel import CustomUserModel


# /mobile/
class LoginTV(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        message = ''

        if request.user.is_authenticated:
            if request.user.role == 'asistente':
                return HttpResponseRedirect('/mobile/dashboard/')
            else:
                return HttpResponseRedirect('/')

        if request.GET.get('show_error'):
            message = 'Error en usuario o conraseña'

        context = self.get_context_data(**kwargs)
        page_data = {
            'title_page': 'Inicio Sesion',
            'module_name': 'Accounts',
            'message': message, 
        }
        return self.render_to_response({**context, **page_data})
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'asistente':
                return HttpResponseRedirect('/mobile/dashboard/')
                return HttpResponseRedirect('/')
        
        return HttpResponseRedirect('/accounts/login/?show_error=true')