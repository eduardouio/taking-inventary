from django.urls import path
from takings.views import StartTakingTP

app_name ='takings'

urlpatterns = [
    #path('', TakingsTP.as_view(), name='list-taking'),
    path('select/<int:id_sap_migration>', StartTakingTP.as_view(), name="seleccionar_migracion"),
]