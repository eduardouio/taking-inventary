from takings.models import TakinDetail, Taking, TakingJustify
from rest_framework.serializers import ModelSerializer


class TakinDetailSerializer(ModelSerializer):
    class Meta:
        model = TakinDetail
        fields = '__all__'


class TakingSerializer(ModelSerializer):
    class Meta:
        model = Taking
        fields = '__all__'


class akingJustifySerializer(ModelSerializer):
    class Meta:
        model = akingJustify
        fields = '__all__'