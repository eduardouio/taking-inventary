from django.urls import path
from takings.views import CreateTakingTP, TakingMasterDetailTV, TakingsList, UpdateTakingCV

app_name ='takings'

urlpatterns = [
    path('master-detail/<int:pk>', TakingMasterDetailTV.as_view(), name='master-detail-taking'),
    path('add-report/', UpdateTakingCV.as_view(), name="update_report"),
    path('create/<int:id_sap_migration>', CreateTakingTP.as_view(), name="selected_migration"),
    path('list/',  TakingsList.as_view(), name="list-migrations"),
]