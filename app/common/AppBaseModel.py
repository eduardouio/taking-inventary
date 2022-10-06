from django.db import models


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

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
