from accounts.models.CustomUserModel import CustomUserModel
from accounts.models.Team import Team
from products.models import Product
from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import TakinDetail, Taking, TakingJustify
from recounts.models import RecountDetails, RecountTakings

from rest_framework.serializers import ModelSerializer


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUserModel
        exclude = ['password']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RecountDetailsSerializer(ModelSerializer):
    class Meta:
        model = RecountDetails
        fields = '__all__'


class RecountTakingsSerializer(ModelSerializer):
    class Meta:
        model = RecountTakings
        fields = '__all__'


class SapMigrationSerializer(ModelSerializer):
    class Meta:
        model = SapMigration
        fields = '__all__'


class SapMigrationDetailSerializer(ModelSerializer):
    class Meta:
        model = SapMigrationDetail
        fields = '__all__'


class TakingDetailSerializer(ModelSerializer):
    class Meta:
        model = TakinDetail
        fields = '__all__'


class TakingSerializer(ModelSerializer):
    class Meta:
        model = Taking
        fields = '__all__'


class TakingJustifySerializer(ModelSerializer):
    class Meta:
        model = TakingJustify
        fields = '__all__'
