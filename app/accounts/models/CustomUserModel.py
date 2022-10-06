from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import CustomUserManager

POSITIONS = (
    ('gestor', 'Gestor Inventario'),
    ('consultor','Consultor Saldos'),
    ('asistente','Asistente Inventario'),
    ('ninguno', 'Sin Acceso'),
)

class CustomUserModel(AbstractUser):
    position = models.CharField(
        'cargo_usuario',
        max_length=40,
        choices=POSITIONS,
        default='ninguno'
    )
    notes = models.CharField(
        'observaciones',
        max_length=250,
        null=True,
        blank=True
    )
    contact = models.CharField(
        'teléfono',
        max_length=12,
        default=None,
        blank=True,
        null=True
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    


    def __str__(self) -> str:
        return self.username