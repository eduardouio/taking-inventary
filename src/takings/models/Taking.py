from django.db import models
from django.conf import settings

from common import AppBaseModel
from accounts.models import CustomUserModel
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
    location = models.CharField(
        'ubicacion_instalaciones',
        max_length=255,
        choices=settings.WARENHOUSES_LOCATIONS_NAME,
        blank=True,
        null=True,
        default=None
    )
    
    def __str__(self):
        return '{}->{}'.format(self.id_taking, self.date)
