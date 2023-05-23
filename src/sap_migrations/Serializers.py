from sap_migrations.models import SapMigration, SapMigrationDetail
from rest_framework.serializers import ModelSerializer


class SapMigrationSerializer(ModelSerializer):
    class Meta:
        model = SapMigration
        fields='__all_-'
    

class SapMigrationDetailSerializer(ModelSerializer):
    class Meta:
        model = SapMigrationDetailSerializer
        fields = '__all__'
