import csv
import random
import string
from faker import Faker
from django.db import IntegrityError

from accounts.models.CustomUserModel import CustomUserModel
from accounts.models.Team import Team
from products.models import Product
from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import Taking, TakinDetail

QUANTITY_OPTIONS = {
    'users': 100,
    'teams': 2000,
    'sap_migrations': 50,
    'takings': 20,
}


class LoadTestData():
    """./manage.py shell < tests/test_data/load_test_data.py"""

    def __init__(self) -> None:
        self.faker = Faker('es_CO')

    def create_super_user(self):
        CustomUserModel.objects.create_superuser(
            username='eduardo',
            password='test.2022'
        )
        print('[OK] creado superuser...')

    def load_users(self):
        for item in range(QUANTITY_OPTIONS['users']):
            user_role = 'asistente'
            if item < 3:
                user_role = 'gestor'
            person_name = self.faker.name()
            pswd = ''.join(random.choices(string.ascii_letters, k=18))
            new_user = {
                'username': person_name.lower().replace(' ', ''),
                'password': pswd,
                'first_name': person_name.split(' ')[0],
                'last_name': person_name.split(' ')[1],
                'email': self.faker.email(),
                'role': user_role,
                'notes': pswd,
            }
            CustomUserModel.objects.create(**new_user)
        print('[OK] Usuarios Insertados...')

    def load_my_users(self):
        users = [
            {'username': 'dayana', 'first_name': 'DAYANA', 'last_name': 'GARCIA',
                'password': '1234.abc', 'email': 'dayana@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'karley', 'first_name': 'KARLEY', 'last_name': 'ZUBIETA',
                'password': '1234.abc', 'email': 'karley@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'johanna', 'first_name': 'JOHANNA', 'last_name': 'PLACES',
                'password': '1234.abc', 'email': 'johanna@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'david', 'first_name': 'DAVID', 'last_name': 'GONZALEZ',
                'password': '1234.abc', 'email': 'david@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'gerardo', 'first_name': 'GERARDO', 'last_name': 'LITA',
                'password': '1234.abc', 'email': 'gerardo@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'mercy', 'first_name': 'MERCY', 'last_name': 'HERNANDEZ',
                'password': '1234.abc', 'email': 'mercy@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'jordan', 'first_name': 'JORDAN', 'last_name': 'DUEÑAS',
                'password': '1234.abc', 'email': 'jordan@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'diego', 'first_name': 'DIEGO', 'last_name': 'GARCIA',
                'password': '1234.abc', 'email': 'diego@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'joel', 'first_name': 'JOEL', 'last_name': 'TITOAÑA',
                'password': '1234.abc', 'email': 'joel@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'isaac', 'first_name': 'ISAAC', 'last_name': 'MALAN',
                'password': '1234.abc', 'email': 'isaac@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'mayra', 'first_name': 'MAYRA', 'last_name': 'AYALA',
                'password': '1234.abc', 'email': 'mayra@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'gaby', 'first_name': 'GABY', 'last_name': 'TOAPANTA',
                'password': '1234.abc', 'email': 'gaby@vinesa.com.ec', 'role': 'asistente'},
            {'username': 'lorena', 'first_name': 'LORENA', 'last_name': 'RODRIGUEZ',
                'password': '1234.abc', 'email': 'lorena@vinesa.com.ec', 'role': 'gestor'},
            {'username': 'alex', 'first_name': 'ALEX', 'last_name': 'LEON',
                'password': '1234.abc', 'email': 'alex@vinesa.com.ec', 'role': 'gestor'},
        ]
        for new_user in users:
            CustomUserModel.objects.create(**new_user)
        print('[OK] Usuarios Insertados...')

    def load_teams(self):
        all_teams = Team.objects.all()
        if len(all_teams):
            print('[Warning] Equipos existentes en la base')
            return None

        for item in range(QUANTITY_OPTIONS['teams']):
            users_assintants = CustomUserModel.objects.filter(
                role='asistente'
            )
            new_team = {
                'group_number': random.randrange(1, 12),
                'manager': users_assintants[random.randrange(1, 95)],
                'warenhouse_assistant': self.faker.name(),
            }
            Team.objects.create(**new_team)
        print('[OK] Equipos creados...')

    def load_products(self):
        file = open('tests/test_data/products.csv', 'r')
        csvreader = csv.reader(file, delimiter=',')
        for line in csvreader:
            type_product = 'otro'
            if 'vino' in line[1].lower():
                type_product = 'vino'
            if 'sauv' in line[1].lower():
                type_product = 'vino'
            if 'tinto' in line[1].lower():
                type_product = 'vino'
            if 'merlot' in line[1].lower():
                type_product = 'vino'
            if 'malbec' in line[1].lower():
                type_product = 'vino'
            if 'espum' in line[1].lower():
                type_product = 'vino'
            if 'carm' in line[1].lower():
                type_product = 'vino'
            if 'chard' in line[1].lower():
                type_product = 'vino'
            if 'blanco' in line[1].lower():
                type_product = 'vino'
            if 'whysky' in line[1].lower():
                type_product = 'espirituoso'
            if 'gin' in line[1].lower():
                type_product = 'espirituoso'
            if 'chinchon' in line[1].lower():
                type_product = 'espirituoso'
            if 'cogñac' in line[1].lower():
                type_product = 'espirituoso'
            if 'pisco' in line[1].lower():
                type_product = 'espirituoso'
            if 'licor' in line[1].lower():
                type_product = 'espirituoso'
            if 'mezcal' in line[1].lower():
                type_product = 'espirituoso'
            if 'tequila' in line[1].lower():
                type_product = 'espirituoso'
            if 'vodka' in line[1].lower():
                type_product = 'espirituoso'
            if 'food' in line[1].lower():
                type_product = 'alimento'
            if 'aceite' in line[1].lower():
                type_product = 'alimento'

            my_product = {
                'account_code': line[0],
                'name': line[1],
                'quantity_per_box': line[3] if line[3] else 1,
                'capacity': line[2] if line[2] else None,
                'ean_13_code': line[4],
                'ean_14_code': line[5],
                'type_product': type_product,
            }
            try:
                Product.objects.create(**my_product)
                print('--> {}'.format(my_product['name']))
            except IntegrityError as e:
                print('ERROR => {} {}'.format(
                    my_product['name'],
                    e.__str__()
                ))
        print('[OK] lista de productos completa...')

    def load_sap_migrations(self):
        for item in range(QUANTITY_OPTIONS['sap_migrations']):
            migration = SapMigration()
            migration.save()

        print('[OK] Migraciones SAP cargadas...')
        all_sap_migrations = SapMigration.objects.all()
        position = True
        for migration in all_sap_migrations:
            print('[INICIANDO] detalle para migracion {}'.format(migration))
            file = open('tests/test_data/detail_migration.csv', 'r')
            csvreader = csv.reader(file, delimiter=',')
            for line in csvreader:
                on_hand = random.randint(-1, 500)
                on_order = random.randint(-1, 500)
                is_commited = random.randint(-1, 50)
                avaliable = (on_hand + on_order - is_commited)

                migration_detail = {
                    'id_sap_migration': migration,
                    'account_code': line[2],
                    'company_name': line[1],
                    'name': line[3],
                    'id_warenhouse_sap_code': line[5],
                    'warenhouse_name': line[6],
                    'on_hand': int(line[7]) if position else on_hand,
                    'on_order': int(line[8]) if position else on_order,
                    'is_commited': int(line[9]) if position else is_commited,
                    'avaliable': (int(line[7]) + int(line[8]) - int(line[9])) if position else avaliable,
                }
                try:
                    SapMigrationDetail.objects.create(**migration_detail)
                except IntegrityError as e:
                    print('Error => {}'.format(e.__str__()))
                    print(migration_detail)
                position = False
            print('[OK] detalles cargados para migracion {}'.format(migration))
        print('[OK] Detalle de migracion Cargada...')

    def unifyPassworwds(self):
        print('actualizamos los password de todos los usuarios')
        all_users = CustomUserModel.objects.all()
        for user in all_users:
            if user.username != 'eduardo' and user.username != 'AnonymousUser':
                user.set_password('1234.abc')
                user.save()
                print('Actializado {}'.format(user.username))


print('---> START LOAD DATA <---')
loadData = LoadTestData()
# loadData.create_super_user()
# loadData.load_users()
# loadData.load_teams()
# loadData.load_products()
# loadData.load_warenhouses()
# loadData.load_sap_migrations()
# loadData.load_takings()
# loadData.load_my_users()
loadData.unifyPassworwds()
print('---> END TASK <---')
