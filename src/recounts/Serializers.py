from recounts.models import RecountDetails, RecountTakings
from rest_framework.serializers import ModelSerializer


class RecountDetailsSerializer(ModelSerializer):
    class Meta:
        model=RecountDetails
        fields='__all__'

class RecountTakingsSerializet(ModelSerializer):
    class Meta:
        model=RecountTakings
        fields='__all__'