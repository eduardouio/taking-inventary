from django.db import models
from common import AppBaseModel
from django.core.exceptions import ObjectDoesNotExist
from common.loggin import loggin


class SapMigration(AppBaseModel):
    id_sap_migration = models.AutoField(
        'id_migracion',
        primary_key=True
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
    have_taking = models.BooleanField(
        'Tiene Toma?',
        default=False,
        blank=True,
        null=True
    )
    report = models.JSONField(
        'Reporte JSON',
        blank=True,
        null=True,
        default=None
    )
    products = models.JSONField(
        'Productos JSON',
        blank=True,
        null=True,
        default=None
    )
    warenhouses = models.JSONField(
        'Bodegas JSON',
        blank=True,
        null=True,
        default=None
    )
    owners = models.JSONField(
        'Empresas JSON',
        blank=True,
        null=True,
        default=None
    )

    def save(self, *args, **kwargs):
        return super(self.__class__, self).save(*args, **kwargs)

    @classmethod
    def get(cls, id_sap_migration):
        try:
           return cls.objects.get(pk=id_sap_migration)
        except ObjectDoesNotExist as e:
            loggin('e', e.__str__())
            return None
    
    def __str__(self) -> str:
        return '{} -> {}'.format(
            self.id_sap_migration,
            self.created
        )
