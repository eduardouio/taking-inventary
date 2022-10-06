from dataclasses import field
from pyexpat import model
from statistics import mode
from django.db import models
from accounts.models import CustomUserModel
from common import AppBaseModel


class TakingModel(AppBaseModel):
    id_taking = models.AutoField(
        'nro toma',
        primary_key=True
    )
    date = models.DateField(
        'fecha toma',
    )
    manager = models.ForeignKey(
        'manager',
        CustomUserModel,
        on_delete=models.RESTRICT
    )
    