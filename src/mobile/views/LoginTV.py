from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from accounts.models.CustomUserModel import CustomUserModel
from common import loggin



# /mobile/
class LoginTV(TemplateView):
    template_name = 'mobile/login.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'mostrando login de mobile')
        message = ''

        if request.user.is_authenticated:
            loggin('i', 'Usuario autencidado redirigiendo')
            return HttpResponseRedirect('/mobile/dashboard/')

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
            login(request=request, user=user)
            loggin('i', 'Usuario Autenticado')
            return HttpResponseRedirect('/mobile/dashboard/')
        
        loggin('w', 'error en autenticacion para {}'.format(username))
        return HttpResponseRedirect('/mobile/?show_error=true')


