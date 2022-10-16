from django.db import models
from common import AppBaseModel
from .SapMigration import SapMigration


class SapMigrationDetail(AppBaseModel):
    id_sap_migration_detail = models.AutoField(
        'id_migracion_detalle',
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
        'codigo_contable',
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    name = models.CharField(
        'nombre_producto',
        max_length=255,
        null=True,
        blank=True,
        default=None
    )
    warenhouse_code = models.PositiveSmallIntegerField(
        'id_bodega',
        null=True,
        blank=True,
        default=None,
    )
    warenhouse_name = models.CharField(
        'nombre_bodega',
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