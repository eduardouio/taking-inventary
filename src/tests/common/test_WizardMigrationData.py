import pytest
from sap_migrations.models import SapMigration
from common import WizardMigrationData


@pytest.mark.django_db
class TestWizardMigrationData:

    def setup_method(self):
        # spected data
        self.spected_data = {
            "sap_migration": SapMigration.get(1),
            "warenhouses": [
                "PAGINA WEB", "BODEGA PRODUCTO MAL ESTADO UIO",
                "VITRINA", "LAGUARDA SAMBORONDON", "LAGUARDA VIA LA COSTA",
                "LAGUARDA CUENCA", "BODEGA MAL ESTADO UIO",
                "MATRIZ PLUSBRAND CUENCA", "CONTROL DE CALIDAD MATRIZ",
                "CONSIGNACIONES PB PROVEEDORES", "CONSIGNACIONES CLIENTES MANTA",
                "ALMACENAMIENTO ALMAGRO", "MATRIZ PLUSBRAND GYE",
                "LAGUARDA EL BOSQUE", "LAGUARDA CUMBAYA", "MATRIZ PLUSBRAND",
                "LAGUARDA", "LAGUARDA MANTA", "CONSIGNACIONES SM PROVEEDORES",
                "CONSIGNACIONES CLIENTES CUENCA", "LAGUARDA PORTUGAL",
                "BODEGA CARCELEN", "ALMACEN 10 DE AGOSTO", "BODEGA PANATLANTIC",
                "Consignaciones Servmultimarc", "BODEGA CUENCA MAL ESTADO",
                "BODEGA GENERAL G8", "Consignaciones Plusbrand",
                "Bodega Rev Ecuador - Carcelén", "Almacen de Consignacion",
                "BODEGA CORDOVEZ CARCELEN", "CONSIGNACIONES CLIENTES",
                "ALMACÉN GENERAL UIO", "ALMACEN GENERAL GYE",
                "MATRIZ PLUSBRAND MANTA",
                "MAL ESTADO GYE", "BODEGA CONSIGNACIONES CLIENTES",
                "ETIQUETAS CFS", "MUESTRAS", "BODEGA CUENCA"
            ],
            "type_products": {
                "ACCESORIOS": ["VARIOS",],
                "LICORES": ["WHISKY", "BAJATIVO", "PISCO", "BRANDY", "VARIOS",
                            "JEREZ", "APERITIVOS", "APERITIVO", "GIN", "RON",
                            "PROMO", "MEZCAL", "TEQUILA", "CHAMPAGNE", "COGNAC",
                            "AGUARDIENTE", "PACKS", "VODKA", "CERVEZA", "VINO",
                            "VARIOS", "CREMA", "ESPUMANTE", "COMBOS", "LICOR",
                            "SANGRIA",
                            ],
                "VARIOS": ["CIGARRILLOS", "ALIMENTOS", "VARIOS"],
            },
            "all_users": 111,
        }
        self.wizard = WizardMigrationData()

    def test_get(self):
        data = self.wizard.get(1)
        assert data['sap_migration'] == self.spected_data['sap_migration']

    def test_get_not_found(self):
        with pytest.raises(Exception):
            self.wizard.get(0)
