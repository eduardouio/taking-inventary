from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from takings.models import Taking
from api.Serializers import TakingSerializer, CustomUserSerializer

from django.contrib.auth import get_user_model as UserModel


# /api/mobile/list/<str:username>/
# name = list-taking-mobile
class ListTakings(ListAPIView):
    serializer_class = TakingSerializer

    def get_queryset(self, username):
        user = get_object_or_404(UserModel(), username=username)

        # obtenemos las ultimas 20 tomas
        return Taking.objects.filter(
            teams__manager=user.pk).order_by('-created')[:20]

    def list(self, request, username, *args, **kwargs):
        """
        Retorna todos los datos necesarios para crear una toma de inventario
        """
        queryset = self.get_queryset(username=username)
        serializer = self.get_serializer(queryset, many=True)
        user = UserModel().objects.get(username=username)
        return Response({
            "takings": serializer.data,
            "user_data": CustomUserSerializer(user).data
        },
            status=status.HTTP_200_OK
        )
