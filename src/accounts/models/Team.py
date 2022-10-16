from django.db import models
from accounts.models import CustomUserModel
from common import AppBaseModel


class Team(AppBaseModel):
    id_team = models.AutoField(
        'id_equipo',
        primary_key=True
    )
    group_number = models.PositiveSmallIntegerField(
        'numero_grupo',
        blank=True,
        null=True,
        default='S/N'
    )
    manager = models.ForeignKey(
        CustomUserModel,
        on_delete=models.PROTECT
    )
    warenhouse_assistant = models.CharField(
        'asistete_bodega',
        max_length = 255,
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return 'grupo #{}->{}'.format(
            self.group_number,
            self.manager
        )
