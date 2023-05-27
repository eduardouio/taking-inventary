import pytest
from takings.lib import ConsolidateTaking


@pytest.mark.django_db
class TestConsolidateTaking:

    def test_get(self):
        spected_data = {
            "id_taking": 1,

        }
