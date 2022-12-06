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
        loggin('i', 'recuperando bodega {}'.format(my_name))
        warenhouses = cls.objects.filter(name=my_name)
        if len(warenhouses):
            for warenhouse in warenhouses:
                if warenhouse.name == my_name:
                    return warenhouse

        return None

    @classmethod
    def get_by_owner(cls, owner_name):
        loggin('i', 'listando bodegas de {}'.format(owner_name))
        warenhouses = cls.objects.filter(owner=owner_name)
        return warenhouses if len(warenhouses) else []
    
    @classmethod
    def get_owners(cls, warenhouse_name):
        loggin('i', 'Listando Propietarios de las bodegas')
        warenhouses = cls.objects.filter(name=warenhouse_name)
        owners = []
        for item in warenhouses:
            owners.append(item.owner)
        
        return owners

    def __str__(self):
        return '{}->{}'.format(
            self.id_warenhouse_sap_code,
            self.name
        )

    class Meta:
        unique_together = [['owner', 'name']]
