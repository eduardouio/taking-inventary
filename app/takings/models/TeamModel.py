from pyexpat import model
from django.db import models
from common import AppBaseModel
from accounts.models import CustomUserModel


class TeamModel(AppBaseModel):
    id_team = models.AutoField(
        'id equipo',
        unique=True
    )
    team = models.ManyToManyField(CustomUserModel)
    pass
    