from accounts.models.CustomUserModel import CustomUserManager
from accounts.models.Team import Team
from rest_framework.serializers import ModelSerializer

class TeamSerializer(ModelSerializer):
    class Meta:
        model= Team
        fields='__all__'

class CustomUserManagerSerializer(ModelSerializer):
    class Meta:
        model = CustomUserManager
        exclude = ['password']