from django.urls import  path
from sap_migrations.views import MigrationTV

app_name='sap.migrations'

urlpatterns = [
    path('', MigrationTV.as_view(), name='list-migrations'),
]   

