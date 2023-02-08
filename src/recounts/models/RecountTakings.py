from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from common import AppBaseModel
from takings.models import Taking

class RecountTakings(AppBaseModel):
    id_recount_taking = models.AutoField(
        'id_reconteo',
        primary_key=True
    )
    id_taking = models.ForeignKey(
        Taking,
        on_delete=models.RESTRICT
    )

    @classmethod
    def get(cls, id_recount):
        try:
            return cls.objects.get(pk=id_recount)
        except ObjectDoesNotExist as e:
            return None
    
    @classmethod
    def get_by_taking(cls, id_taking):
        query = cls.objects.filter(id_taking_id = id_taking)
        if query:
            return query
        return []
    
    def __str__(self) -> str:
        return self.id_taking