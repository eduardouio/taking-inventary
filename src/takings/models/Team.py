from django.db import models
from common import AppBaseModel
from accounts.models import CustomUserModel
from .Taking import Taking

class Team(AppBaseModel):
    id_team = models.AutoField(
        'id equipo',
        primary_key=True
    )
    id_taking = models.ForeignKey(
        Taking,
        on_delete=models.CASCADE
    )
    user_manager_team = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE
    )
    warenhouse_team = models.CharField(
        'personal bodega',
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    
    def __str__(self):
        return {'{}->{} / {}'.format(
            self.pk,
            self.user_manager_team,
            self.warenhouse_team
        )}    