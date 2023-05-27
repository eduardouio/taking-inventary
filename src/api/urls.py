from django.urls import path
from api.views import AllTakingDataAPIView


urlpatterns = [
    path('all-taking-data/<id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"),
]
