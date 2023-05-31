from django.urls import path
from api.views.common.AllTakingDataAPIView import AllTakingDataAPIView
from api.views.takings.UpdateTakingAPIView import UpdateTakingAPIView
from api.views.accounts.UpdateTeamAPIView import UpdateTeamAPIView, CreateTeamAPIView


urlpatterns = [
    path('common/taking-data/<id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"
         ),
    path('takings/update-taking/<id_taking>/',
         UpdateTakingAPIView.as_view(), name="update_taking"
         ),
    path('teams/update-team/<id_team>/',
         UpdateTeamAPIView.as_view(), name="update_taking"
         ),
    path('teams/create-team/',
         CreateTeamAPIView.as_view(),
         name="create_team"
         ),
]
