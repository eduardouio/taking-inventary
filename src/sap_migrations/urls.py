from django.urls import  path
from sap_migrations.views import MigrationListTV, DetailMigrationsTV

app_name='sap.migrations'

urlpatterns = [
    path('', MigrationTV.as_view(), name='list-migrations'),
    path('detail/<int:pk>', DetailMigrationsTV.as_view(), name='detail-migration'),
]   

