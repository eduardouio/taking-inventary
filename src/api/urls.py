from django.urls import path
from api.views import AllTakingDataAPIView, UpdateTakingAPIView


urlpatterns = [
    path('all-taking-data/<id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"),
    path('update-taking/<id_taking>/',
         UpdateTakingAPIView.as_view(), name="update_taking"),
]
