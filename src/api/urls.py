from django.urls import path
from api.views.common.AllTakingDataAPIView import AllTakingDataAPIView
from api.views.takings.UpdateTakingAPIView import UpdateTakingAPIView


urlpatterns = [
    path('common/taking-data/<id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"),
    path('takings/update-taking/<id_taking>/',
         UpdateTakingAPIView.as_view(), name="update_taking"),
]
