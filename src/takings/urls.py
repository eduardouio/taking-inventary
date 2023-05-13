from django.urls import path
from takings.views import (CreateTakingTP,
                           TakingMasterDetailTV,
                           TakingsList,
                           UpdateTakingCV,
                           APITakingDetail,
                           APITaking,
                           APITakingManager
                           )

app_name = 'takings'

urlpatterns = [
    path('',  TakingsList.as_view(), name="list-migrations"),
    path('detail/<int:pk>', TakingMasterDetailTV.as_view(),
         name='master-detail-taking'),
    path('add-report/', UpdateTakingCV.as_view(), name="update_report"),
    path('create/<int:id_sap_migration>',
         CreateTakingTP.as_view(), name="selected_migration"),
    path('api/taking-detail/taking/<int:id_taking>/product/<str:id_product>/',
         APITakingDetail.as_view(), name="detail_migration_api"),
    path('api/taking/<int:id_taking>/', APITaking.as_view(), name="taking_api"),
    path('api/taking-manager/<int:id_taking>/',
         APITakingManager.as_view(), name="taking_manager_api"),
]
