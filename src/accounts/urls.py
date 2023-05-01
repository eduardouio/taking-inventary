from django.urls import path
from accounts.views import LoginTV, LogoutRV, APIupdateTeam

app_name = 'accounts'

urlpatterns = [
    path('login', LoginTV.as_view(), name='accounts-login'),
    path('login/', LoginTV.as_view(), name='accounts-login'),
    path('logout/', LogoutRV.as_view(), name="accounts-logout"),
    path('update-team/', APIupdateTeam.as_view(), name="accounts-update-team"),
]
