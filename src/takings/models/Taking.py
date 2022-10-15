from django.db import models
from crum import get_current_user

from common import AppBaseModel
from warenhouses.models import Warenhouse
from accounts.models import CustomUserModel


class Taking(AppBaseModel):
    id_taking = models.AutoField(
        'nro toma',
        primary_key=True
    )
    date = models.DateField(
        'fecha toma',
    )
    hour_start = models.TimeField(
        'hora inicio',
        blank=True,
        null=True,
        default=None
    )
    id_user_manager = models.PositiveSmallIntegerField(
        'id user manager',
        default=None,
        blank=True,
        null=True
    )
    hour_end = models.TimeField(
        'hora fin',
        blank=True,
        null=True,
        default=None
    )
    warenhouses = models.ManyToManyField(
        Warenhouse
    )
    participans = models.ManyToManyField(
        CustomUserModel
    )
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        
        if user is None:
            return super(Taking, self).save(*args, **kwargs)
        
        if not self.pk:
            self.id_user_created = user.pk
        
        self.id_user_updated = user.pk
        return super(Taking, self).save(*args, **kwargs)
    
    def __str__(self):
        return '{}->{}'.format(self.id_taking, self.date)
