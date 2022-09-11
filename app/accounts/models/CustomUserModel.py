from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import CustomUserManager

POSITIONS = (
    ('gestor', 'Gestor Inventario'),
    ('consultor','Consultor Saldos'),
    ('asistente','Asistente Incentario'),
    ('ninguno', 'Sin Acceso'),
)

class CustomUserModel(AbstractUser):
    position = models.CharField(
        'cargo_usuario',
        max_length=40,
        choices=POSITIONS,
        default='ninguno'
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    


    def __str__(self) -> str:
        return self.username