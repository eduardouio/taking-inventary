from simple_history.models import HistoricalRecords
from django.db import models

from common import AppBaseModel


class Warenhouse(AppBaseModel):

    id_warenhouse = models.AutoField(
        'ID Bodega',
        primary_key=True
    )

    id_warenhouse_number = models.PositiveSmallIntegerField(
        'identificador bodega SAP',
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
        'notas adicionales',
        null=True,
        blank=True,
        default=None
    )

    history = HistoricalRecords()

    def __str__(self):
        return '{}-{}'.format(
            self.id_warenhouse_number,
            self.enterprise_name
        )

    class Meta:
        unique_together = [['ruc_enterprise', 'name']]
