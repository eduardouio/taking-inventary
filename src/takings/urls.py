from django.urls import path
from takings.views import StartTakingTP, TakingMobile

app_name ='takings'

urlpatterns = [
    #path('', TakingsTP.as_view(), name='list-taking'),
    path('select/<int:id_sap_migration>', StartTakingTP.as_view(), name="selected_migration"),
    path('taking/<int:id_sap_migration>', TakingMobile.as_view(), name="start_read"),
]