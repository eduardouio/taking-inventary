from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from accounts.managers import CustomUserManager
from common import loggin

ROLES = (
    ('gestor', 'Gestor Inventario'),
    ('consultor','Consultor Saldos'),
    ('asistente','Asistente Inventario'),
    ('auditor','Auditor Inventario'),
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
        upload_to = 'users/images/profile_picture',
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
    @classmethod
    def get_user_public_data(cls, username):
        user = cls.get(username)
        if user is None:
            raise Exception('Usuario no registrado, no procede toma')
        public_data = {
            'id': user.id,
            'last_login': user.last_login.isoformat(),
            'is_superuser': user.is_superuser,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined.isoformat(),
            'role': user.role,
            'notes': user.notes,
            'contact': user.contact,
            'dni_number': user.dni_number,
            'picture': user.picture,
        }
        return public_data

    def __str__(self) -> str:
        return self.username