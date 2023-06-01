from django.urls import path
from api.views.common import AllTakingDataAPIView, AddTeamTakingAPIView
from api.views.takings.UpdateTakingAPIView import UpdateTakingAPIView
from api.views.accounts.UpdateTeamAPIView import UpdateTeamAPIView


urlpatterns = [
    path('common/taking-data/<int:id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"
         ),
    path('takings/update-taking/<id_taking>/',
         UpdateTakingAPIView.as_view(), name="update_taking"
         ),
    path('teams/update-team/<id_team>/',
         UpdateTeamAPIView.as_view(), name="update_taking"
         ),
    path('takings/add-team-taking/<int:id_taking>/',
         AddTeamTakingAPIView.as_view(), name="add-team-taking"),

]
