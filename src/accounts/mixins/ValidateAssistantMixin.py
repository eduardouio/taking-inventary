from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ValidateAssistantMixin(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        if request.user.role != 'asistente':
            return redirect('/accounts/logout/')
        
        return super().dispatch(request, *args, **kwargs)
