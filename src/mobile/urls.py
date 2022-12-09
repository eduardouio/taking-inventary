from django.urls import path
from .views import LoginTV, DashboarTV, Taking


app_name = 'mobile'

urlpatterns = [
    path('', LoginTV.as_view(), name="mobile-login"),
    path('dashboard/', DashboarTV.as_view(), name='mobile-dashboard'),
    path('taking/<int:id_taking>/', Taking.as_view(), name='mobile-taking'),
]