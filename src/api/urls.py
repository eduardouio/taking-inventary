from django.urls import path

from api.views.accounts.UpdateTeamAPIView import UpdateTeamAPIView
from api.views.common import (AddTeamTakingAPIView, AllTakingDataAPIView,
                              RecountAPIView, TakingMigrationAPIView, WizardAPIView, ReportManagerAPIView)
from api.views.takings.UpdateTakingAPIView import UpdateTakingAPIView
from api.views.takings_detail import DeleteTakingDetailAPIView
from api.views.sap_migrations import AllSAPMigrationData
from api.views.mobile import ListTakings, TakingAssistantInput

urlpatterns = [
    # vistas comunes
    path('common/taking-data/<int:id_taking>/',
         AllTakingDataAPIView.as_view(), name="all_taking_data"
         ),
    path('common/taking-migration/taking/<int:id_taking>/product/<str:account_code>/',
         TakingMigrationAPIView.as_view(), name="taking_migration"
         ),
    path('common/add-team-taking/<int:id_taking>/',
         AddTeamTakingAPIView.as_view(), name="add-team-taking"
         ),
    path('common/recount/<int:id_taking>/<str:account_code>/',
         RecountAPIView.as_view(), name="recount-taking"
         ),
    path('common/wizard-assistant/<int:id_sap_migration>/',
         WizardAPIView.as_view(), name="wizard-assistant"
         ),
    # tomas de inventario
    path('takings/update-taking/<int:id_taking>/',
         UpdateTakingAPIView.as_view(), name="update_taking"
         ),
    # equipos
    path('teams/update-team/<int:id_team>/',
         UpdateTeamAPIView.as_view(), name="update-team"
         ),
    # tomas de inventario detalle
    path('takings-detail/delete/<int:id_taking_detail>/',
         DeleteTakingDetailAPIView.as_view(), name="delete-taking-detail"
         ),
    # migraciones
    path('migrations/new-report/',
         AllSAPMigrationData.as_view(), name="all-sap-migration-data"
         ),
    # asistente Toma Mobile
    path('mobile/list/<str:username>/',
         ListTakings.as_view(), name="list-taking-mobile"
         ),
    path('mobile/assistant/id_tk/<int:id_taking>/id_tm/<int:id_team>/',
         TakingAssistantInput.as_view(), name="api-assistant-input"
         ),
     # reportes
     path('report-manager/taking/<int:id_taking>/',
         ReportManagerAPIView.as_view(), name="api-manager-report"
         ),
]
