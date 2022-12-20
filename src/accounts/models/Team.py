from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from accounts.models.CustomUserModel import CustomUserModel
from common import AppBaseModel, loggin


class Team(AppBaseModel):
    id_team = models.AutoField(
        'id equipo',
        primary_key=True
    )
    group_number = models.PositiveSmallIntegerField(
        'numero grupo',
        blank=True,
        null=True,
        default='S/N'
    )
    manager = models.ForeignKey(
        CustomUserModel,
        on_delete=models.PROTECT
    )
    warenhouse_assistant = models.CharField(
        'asistete bodega',
        max_length = 255,
        blank=True,
        null=True,
        default=None
    )
    id_taking = models.PositiveIntegerField(
        'id toma',
    )

    @classmethod
    def get(cls, id_team):
        try:
            return cls.objects.get(pk=id_team)
        except ObjectDoesNotExist as e:
            return None

    @classmethod
    def get_by_taking(cls, id_taking):
        teams = cls.objects.filter(id_taking=id_taking)
        if teams:
            return teams
        return []
    
    @classmethod
    def get_teams_by_user(cls, username):
        teams = cls.objects.filter(manager=username)
        if teams:
            return teams 
        return []

        

    def __str__(self):
        return 'grupo #{}->Manager {}'.format(
            self.group_number,
            self.manager
        )
 