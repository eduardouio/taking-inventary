from django.db import models
from common import AppBaseModel


class SapMigration(AppBaseModel):
    id_sap_migration = models.AutoField(
        'id_migracion',
        primary_key=True
    )
    
    def save(self, *args, **kwargs):
        return super(self.__class__, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return '{}->{}'.format(
            self.id_sap_migration,
            self.created
        )
