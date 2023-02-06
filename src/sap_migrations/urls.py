from django.urls import path
from sap_migrations.views import MigrationListTV, DetailMigrationsTV, APISapMigrationDetail

app_name = 'sap.migrations'

urlpatterns = [
    path('', MigrationListTV.as_view(), name='list-migrations'),
    path('detail/<int:pk>', DetailMigrationsTV.as_view(), name='detail-migration'),
    path('api/migration/<int:id_migration>/taking/<int:id_taking>/product/<str:id_product>',
         APISapMigrationDetail.as_view(), name='detail-migration-product'),
]
