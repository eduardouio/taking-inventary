from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from common import AppBaseModel, loggin
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
    id_warenhouse_sap_code = models.CharField(
        'identificador_sap',
        max_length=10,
        blank=True,
        null=True,
        default=None
    )
    warenhouse_name = models.CharField(
        'nombre bodega',
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
    on_hand = models.IntegerField(
        'stock',
        default=0,
        null=True,
        blank=True
    )
    on_order = models.IntegerField(
        'solicitado',
        default=0,
        null=True,
        blank=True
    )
    is_commited = models.IntegerField(
        'comprometido',
        default=0,
        null=True,
        blank=True
    )
    avaliable = models.IntegerField(
        'saldo',
        default=0,
        null=True,
        blank=True
    )
    
    @classmethod
    def get_by_migration(cls, id_migration):
        detail = cls.objects.filter(id_sap_migration=id_migration)
        if len(detail):
            return list(detail)
        
        loggin('w', 'Sapmigration {} no tiene detalles'.format(id_migration))
        return []
    
    @classmethod
    def get(cls, id_sap_migration_detail):
        try:
            return cls.objects.get(pk=id_sap_migration_detail)
        except ObjectDoesNotExist as e:
            loggin('e', e.__str__())
            return None
            
    def __str__(self):
        return '{}->{}'.format(self.name, self.on_hand)