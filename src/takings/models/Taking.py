from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from common import AppBaseModel
from accounts.models.CustomUserModel import CustomUserModel
from accounts.models.Team import Team
from sap_migrations.models import SapMigration
from warenhouses.models import Warenhouse


class Taking(AppBaseModel):
    id_taking = models.AutoField(
        'nro toma',
        primary_key=True
    )
    id_sap_migration = models.ForeignKey(
        SapMigration,
        on_delete=models.PROTECT
    )
    hour_start = models.TimeField(
        'hora inicio',
        blank=True,
        null=True,
        default=None
    )
    hour_end = models.TimeField(
        'hora fin',
        blank=True,
        null=True,
        default=None
    )
    user_manager = models.ForeignKey(
        CustomUserModel,
        on_delete=models.PROTECT    
    )
    warenhouses = models.ManyToManyField(
        Warenhouse
    )
    teams = models.ManyToManyField(
        Team
    )
    location = models.CharField(
        'ubicacion instalaciones',
        max_length=255,
        choices=settings.WARENHOUSES_LOCATIONS_NAME,
        blank=True,
        null=True,
        default=None
    )
    total_warenhouses = models.PositiveIntegerField(
        'Total Bodegas',
        default=0,
        null=True,
        blank=True
    )
    total_products_unities = models.PositiveIntegerField(
        'Total Items',
        default=0,
        null=True,
        blank=True
    )
    total_groups = models.PositiveIntegerField(
        'Total Grupos',
        default=0,
        null=True,
        blank=True
    )
    total_products = models.PositiveIntegerField(
        'total Productos',
        default=0,
        null=True,
        blank=True
    )
    have_report = models.BooleanField(
        'Tiene Reporte?',
        default=False,
        blank=True,
        null=True
    )

    @classmethod
    def get(cls, id_taking):
        try:
            return cls.objects.get(pk=id_taking)
        except ObjectDoesNotExist as e:
            return None

    def __str__(self):
        return '{}->{}->{}'.format(
            self.id_taking, 
            self.user_manager,
            self.created
           )