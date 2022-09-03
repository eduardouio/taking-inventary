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

    id_user = models.PositiveSmallIntegerField(
        'Usuario',
        default=1,
        null=True,
        blank=True,
        help_text="Nombre del usuario que realiza el registro"
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
