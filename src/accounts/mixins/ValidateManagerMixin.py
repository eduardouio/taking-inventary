from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ValidateManagerMixin(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        if not request.user.is_anonymous:
            if request.user.role == 'asistente':
                return redirect('/accounts/logout/')
            
        return super().dispatch(request, *args, **kwargs)
