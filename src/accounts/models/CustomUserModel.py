from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from common import loggin
from accounts.managers import CustomUserManager

ROLES = (
    ('gestor', 'Gestor Inventario'),
    ('consultor','Consultor Saldos'),
    ('asistente','Asistente Inventario'),
    ('ninguno', 'Sin Acceso'),
)


class CustomUserModel(AbstractUser):
    role = models.CharField(
        'cargo',
        max_length=40,
        choices=ROLES,
        default='ninguno'
    )
    notes = models.CharField(
        'observaciones',
        max_length=250,
        null=True,
        blank=True
    )
    contact = models.CharField(
        'telefono',
        max_length=12,
        default=None,
        blank=True,
        null=True
    )
    dni_number = models.CharField(
        'numero de cedula',
        max_length=25,
        blank=True,
        null=True,
        default=None,
    )
    picture = models.ImageField(
        'imagen perfil',
        upload_to = 'media/src/images/profile_picture',
        blank=True,
        null=True,
        default=None
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    @classmethod
    def get(cls,username):
        try:
            return cls.objects.get(username=username)
        except ObjectDoesNotExist as o:
            loggin('i', 'Error al obtener el usuario {} '.format(
                username
            ))
            return None

    def __str__(self) -> str:
        return self.username