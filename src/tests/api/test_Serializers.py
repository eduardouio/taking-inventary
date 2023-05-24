import pytest
from api import (CustomUserManagerSerializer, ProductSerializer,
                             RecountDetailsSerializer,
                             RecountTakingsSerializet,
                             SapMigrationDetailSerializer,
                             SapMigrationSerializer, TakinDetailSerializer,
                             TakingJustifySerializer, TakingSerializer,
                             TeamSerializer)


@pytest.mark.django_db
class TestSerializers:
    assert(False, True)