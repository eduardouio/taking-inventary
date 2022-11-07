from django.db import models
from common import AppBaseModel
from accounts.models import CustomUserModel
from django.conf import settings
from common import loggin

class Warenhouse(AppBaseModel):
    """Warenhouse ERP"""
    id_warenhouse = models.AutoField(
        'id_bodega',
        primary_key=True
    )
    id_warenhouse_sap_code = models.CharField(
        'identificador_sap',
        max_length=10,
        blank=True,
        null=True,
        default=None
    )
    name = models.CharField(
        'nombre_bodega',
        max_length=100,
    )
    owner = models.CharField(
        'empresa',
        max_length=100,
        choices=settings.ENTERPRISES_TAKING
    )
    location = models.CharField(
        'ubicación_bodega',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    area_m2 = models.PositiveSmallIntegerField(
        'area_metros',
        blank=True,
        null=True,
        default=None
    )
    capacity = models.PositiveIntegerField(
        'capacidad en cajas de 12',
        blank=True,
        null=True,
        default=0
    )
    
    @classmethod
    def get_by_name(cls, my_name):
        loggin('i', 'recuperando bidega {}'.format(my_name))
        warenhouses = cls.objects.filter(name=my_name)
        return warenhouses if len(warenhouses) else None

    def __str__(self):
        return '{}-{}'.format(
            self.id_warenhouse_number,
            self.owner
        )

    class Meta:
        unique_together = [['owner', 'name']]
