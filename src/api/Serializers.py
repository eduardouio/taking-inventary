from accounts.models.CustomUserModel import CustomUserManager
from accounts.models.Team import Team
from products.models import Product
from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import TakinDetail, Taking, TakingJustify
from recounts.models import RecountDetails, RecountTakings

from rest_framework.serializers import ModelSerializer

class TeamSerializer(ModelSerializer):
    class Meta:
        model= Team
        fields='__all__'


class CustomUserManagerSerializer(ModelSerializer):
    class Meta:
        model = CustomUserManager
        exclude = ['password']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'


class RecountDetailsSerializer(ModelSerializer):
    class Meta:
        model=RecountDetails
        fields='__all__'

class RecountTakingsSerializet(ModelSerializer):
    class Meta:
        model=RecountTakings
        fields='__all__'


class SapMigrationSerializer(ModelSerializer):
    class Meta:
        model = SapMigration
        fields='__all_-'
    

class SapMigrationDetailSerializer(ModelSerializer):
    class Meta:
        model = SapMigrationDetailSerializer
        fields = '__all__'


class TakinDetailSerializer(ModelSerializer):
    class Meta:
        model = TakinDetail
        fields = '__all__'


class TakingSerializer(ModelSerializer):
    class Meta:
        model = Taking
        fields = '__all__'


class TakingJustifySerializer(ModelSerializer):
    class Meta:
        model = akingJustify
        fields = '__all__'