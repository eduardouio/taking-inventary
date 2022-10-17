from django.db import models
from common import AppBaseModel
from .SapMigration import SapMigration


class SapMigrationDetail(AppBaseModel):
    id_sap_migration_detail = models.AutoField(
        'id detalle',
        primary_key=True
    )
    id_sap_migration = models.ForeignKey(
        SapMigration,
        on_delete=models.PROTECT
    )
    company_name = models.CharField(
        'propietario',
        max_length=250,
        null=True,
        blank=True,
        default=None
    )
    account_code = models.CharField(
        'codigo contable',
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    name = models.CharField(
        'nombre producto',
        max_length=255,
        null=True,
        blank=True,
        default=None
    )
    warenhouse_code = models.PositiveSmallIntegerField(
        'id bodega',
        null=True,
        blank=True,
        default=None,
    )
    warenhouse_name = models.CharField(
        'nombre bodega',
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
    on_hand = models.PositiveIntegerField(
        'stock',
        default=0,
        null=True,
        blank=True
    )
    on_order = models.PositiveIntegerField(
        'solicitado',
        default=0,
        null=True,
        blank=True
    )
    is_commited = models.PositiveIntegerField(
        'comprometido',
        default=0,
        null=True,
        blank=True
    )
    avaliable = models.PositiveIntegerField(
        'saldo',
        default=0,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return '{}->{}'.format(self.name, self.on_hand)