from django.db import models


class AppBaseModel(models.Model):
    """Base model for all app model"""
    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='DateTime when the object was created'
    )

    modified = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text='DateTime for last modefied object'
    )

    is_active = models.BoleanField(
        'is_active',
        default=True,
        null=True,
        blank=True,
        help_text="Indica si es un registro activo"
    )

    id_user = models.SmallPositiveIntegerField(
        'id_user',
        default=1,
        null=True,
        blank=True,
        help_text="Nombre del usuario que realiza el registro"
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
