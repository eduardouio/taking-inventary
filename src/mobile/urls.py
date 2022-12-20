from django.urls import path
from .views import DashboarTV, TakingTV


app_name = 'mobile'

urlpatterns = [
    path('dashboard/', DashboarTV.as_view(), name='mobile-dashboard'),
    path('taking/<int:id_taking>/', TakingTV.as_view(), name='mobile-taking'),
]