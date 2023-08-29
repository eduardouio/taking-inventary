from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ValidateAuditorMixin(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')

        if not request.user.is_anonymous:
            if request.user.role != 'admin' and request.user.role != 'auditor':
                return redirect('/accounts/logout/')
            
        return super().dispatch(request, *args, **kwargs)
