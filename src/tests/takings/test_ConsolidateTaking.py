import pytest
from takings.lib import ConsolidateTaking


@pytest.mark.django_db
class TestConsolidateTaking:

    def setup_method(self):
        self.consolidate = ConsolidateTaking()

    def test_get(self):
        # obtenemos la data del wizard y la migracion esperada
        assert 1 == 2
