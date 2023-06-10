from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from common import AppBaseModel
from accounts.models.CustomUserModel import CustomUserModel
from accounts.models.Team import Team
from sap_migrations.models import SapMigration


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
    warenhouses = models.JSONField(
        blank=True,
        null=True,
        default=None
    )
    teams = models.ManyToManyField(
        Team
    )
    name = models.TextField(
        'nombre',
        max_length=255,
        blank=True,
        null=True,
        default=None
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
    date_end_taking = models.DateTimeField(
        'Fecha Cierre Toma',
        blank=True,
        null=True,
        default=None
    )
    date_audit = models.DateTimeField(
        'Fecha revision Audoitoria',
        blank=True,
        null=True,
        default=None
    )
    audit_comments = models.CharField(
        'Comentarios Auditoria',
        max_length=1200,
        blank=True,
        null=True,
        default=None
    )
    is_it_audited = models.BooleanField(
        '¿Auditado?',
        blank=True,
        null=True,
        default=False
    )

    @classmethod
    def get(cls, id_taking):
        try:
            return cls.objects.get(pk=id_taking)
        except ObjectDoesNotExist as e:
            return None

    @classmethod
    def get_by_team(cls, id_team):
        takings = cls.objects.filter(teams__id_team=id_team)
        if takings:
            return takings.first()
        return None

    @classmethod
    def get_by_sap_migrations(cls, id_sap_migration):
        takings = cls.objects.filter(id_sap_migration=id_sap_migration)
        if takings:
            return takings
        return []

    def __str__(self):
        return '{}->{}->{}'.format(
            self.id_taking,
            self.user_manager,
            self.created
        )
