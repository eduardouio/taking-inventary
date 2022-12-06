from django.urls import path
from takings.views import CreateTakingTP, TakingMobile, TakingMasterDetailTV

app_name ='takings'

urlpatterns = [
    path('master-detail/<int:pk>', TakingMasterDetailTV.as_view(), name='master-detail-taking'),
    path('create/<int:id_sap_migration>', CreateTakingTP.as_view(), name="selected_migration"),
    path('register-taking/<int:id_sap_migration>', TakingMobile.as_view(), name="start_read"),
]