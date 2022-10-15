from django.db import models
from common import AppBaseModel

class Warenhouse(AppBaseModel):
    id_warenhouse = models.AutoField(
        'id_bodega',
        primary_key=True
    )

    id_warenhouse_number = models.PositiveSmallIntegerField(
        'identificador_sap',
    )
    enterprise_name = models.CharField(
        'empresa',
        max_length=100,
        help_text='Nombre de la empresa a la que pertense'
    )
    ruc_enterprise = models.CharField(
        'ruc_empresa',
        max_length=13,
        help_text='Ruc de la empresa propietaria de la bodega'
    )
    name = models.CharField(
        'nombre_bodega',
        max_length=100,
        help_text='Nombre de la bodega'
    )
    notes = models.TextField(
        'notas_adicionales',
        null=True,
        blank=True,
        default=None
    )
    location_warenhouse = models.CharField(
        'ubicación_bodega',
        max_length=100,
        null=True,
        blank=True,
        default=None
    )
    admin_warenhouse = models.CharField(
        'administrador_bodega',
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    owner_warenhouse = models.CharField(
        'empresa propietaria',
        max_length=100,
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

    def __str__(self):
        return '{}-{}'.format(
            self.id_warenhouse_number,
            self.enterprise_name
        )

    class Meta:
        unique_together = [['ruc_enterprise', 'name']]
