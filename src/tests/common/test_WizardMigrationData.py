import pytest
from sap_migrations.models import SapMigration
from common.WizardMigrationData import WizardMigrationData


@pytest.mark.django_db
class TestWizardMigrationData:

    def setup_method(self):
        # spected data

        self.lend_data = {
            "sap_migration": 1,
            "warenhouses": 40,
            "warenhouses_owners": 40,
            "type_products": 33,
            "all_users": 122,
            "products": 1437,
        }

        self.spected_data = {
            "sap_migration": SapMigration.get(1),
            "warenhouses": [
                "PAGINA WEB", "BODEGA PRODUCTO MAL ESTADO UIO",
                "VITRINA", "LAGUARDA SAMBORONDON", "LAGUARDA VIA LA COSTA",
                "LAGUARDA CUENCA", "BODEGA MAL ESTADO UIO"
            ],
            "warenhouses_owners": [
                "AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.",
                "CORPORACIÓN PLUSBRAND DEL ECUADOR CIA. LTDA.",
                "IMNAC IMPORTADORA NACIONAL CIA LTDA",
                "REV ECUADOR S.A",
                "SERVMULTIMARC CIA. LTDA.",
                "VIDINTERNACIONAL S.A.",
                "VINOS Y ESPIRITUOSOS DEL LITORAL VINLITORAL S.A.",
                "VINOS Y ESPIRITUOSOS VINESA S.A",
            ],
            # sample type products
            "type_products": ['ACCESORIOS', 'BAJATIVO','LICORES', 'VARIOS'],
            # sample users
            "all_users": ['evillota', 'vpadilla', 'jgarcia',],
            # sample products
            "products": [
                "WHISKY SOMETHING SPECIAL",
                "RON HAVANA CLUB AÑEJO 3 AÑOS",
                "VINO RESERVADO CABERNET",
            ],

        }
        self.wizard = WizardMigrationData()

    def test_get(self):
        # obtenemos la data del wizard y la migracion esperada
        migration = SapMigration.get(1)
        wizard_data = self.wizard.get(1)

        # verificamos los keys
        assert set(wizard_data.keys()) == set(self.spected_data.keys())

        # verificamos la migracion
        assert wizard_data['sap_migration'] == migration

        # verificamos la cantidad de reistros por key
        assert len(wizard_data['warenhouses']) == self.lend_data['warenhouses']
        assert len(wizard_data['warenhouses_owners']
                   ) == self.lend_data['warenhouses_owners']
        assert len(wizard_data['type_products']
                   ) == self.lend_data['type_products']
        assert len(wizard_data['all_users']) == self.lend_data['all_users']
        assert len(wizard_data['products']) == self.lend_data['products']

        # verificamos la warenhouses
        for warenhouse in self.spected_data['warenhouses']:
            assert warenhouse in wizard_data['warenhouses']

        # Verificamos los owner de las bodegas
        owners = [w['owners'] for w in wizard_data['warenhouses_owners']]
        owners = set([elem for sub_list in owners for elem in sub_list])
        owners = [o for o in sorted(owners)]

        assert owners == self.spected_data['warenhouses_owners']

        # Verificamos los type products
        type_products = [w['type_product']
                         for w in wizard_data['type_products']]
        type_products = set([item.split(';')[0] for item in type_products])
        type_products = [o for o in sorted(type_products)]
        assert type_products == self.spected_data['type_products']

        # Verificamos los users
        users = [w['username'] for w in wizard_data['all_users']]
        for spected_user in self.spected_data['all_users']:
            assert spected_user in users

        # Verificamos los products
        products = [w['name'] for w in wizard_data['products']]
        for spected_product in self.spected_data['products']:
            assert spected_product in products

    def test_get_not_found(self):
        with pytest.raises(Exception):
            self.wizard.get(0)
