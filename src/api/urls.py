from django.urls import path
from api.views.common import AllTakingDataAPIView, AddTeamTakingAPIView, TakingMigrationAPIView
from api.views.takings.UpdateTakingAPIView import UpdateTakingAPIView
from api.views.accounts.UpdateTeamAPIView import UpdateTeamAPIView


urlpatterns = [
    path('common/taking-data/<int:id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"
         ),
    path('common/taking-migration/taking/<int:id_taking>/product/<str:account_code>/',
         TakingMigrationAPIView.as_view(), name="taking_migration"
         ),
    path('common/add-team-taking/<int:id_taking>/',
         AddTeamTakingAPIView.as_view(), name="add-team-taking"),
    path('takings/update-taking/<int:id_taking>/',
         UpdateTakingAPIView.as_view(), name="update_taking"
         ),
    path('teams/update-team/<int:id_team>/',
         UpdateTeamAPIView.as_view(), name="update_taking"
         ),

]
