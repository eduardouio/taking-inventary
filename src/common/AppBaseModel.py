from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from simple_history.models import HistoricalRecords
from crum import get_current_user

from accounts.models.CustomUserModel import CustomUserModel


class AppBaseModel(models.Model):
    """Base model for all app model"""
    created = models.DateTimeField(
        'Fecha Registro',
        auto_now_add=True,
        help_text='DateTime when the object was created'
    )

    modified = models.DateTimeField(
        'Cambiado',
        auto_now=True,
        help_text='DateTime for last modefied object'
    )

    is_active = models.BooleanField(
        'Está Activa?',
        default=True,
        help_text=(
            'Indica si es un registro activo, si no se marca la casilla '
            'es un registro inactivo'
        )
    )

    id_user_created = models.PositiveSmallIntegerField(
        'Creeado Por',
        default=1,
        null=True,
        blank=True,
        help_text="Nombre del usuario que realiza el registro"
    )
    
    id_user_updated = models.PositiveSmallIntegerField(
        'Actualizado Por',
        default=1,
        null=True,
        blank=True,
        help_text="Nombre del usuario que realiza el registro"
    )

    notes = models.CharField(
        'observaciones',
        max_length=400,
        blank=True,
        null=True,
        default=None
    )
    history = HistoricalRecords(inherit=True)
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is None:
            return super().save(*args, **kwargs)

        if not self.pk:
            self.id_user_created = user.pk

        self.id_user_updated = user.pk
        return super().save(*args, **kwargs)

    def get_user(self):
        users = {
            'create_by':None,
            'update_by':None,
        }

        try:
            users['create_by'] = CustomUserModel.objects.get(
                pk=self.id_user_created
            )
        except ObjectDoesNotExist:
            pass
        
        try:
            if self.id_user_updated is None:
                users['update_by'] = None
            else:
                users['update_by'] = CustomUserModel.objects.get(
                    pk=self.id_user_updated
                )
        except ObjectDoesNotExist:
            pass

        return users

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
