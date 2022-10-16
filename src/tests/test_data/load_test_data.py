import csv
import random
import string
from faker import Faker
from django.db import IntegrityError

from accounts.models import CustomUserModel, Team
from products.models import Product
from warenhouses.models import Warenhouse
from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import Taking, TakinDetail

class LoadTestData():
    
    def __init__(self) -> None:
        self.faker = Faker()

    def create_super_user(self):
        CustomUserModel.objects.create_superuser(
            username= 'eduardo',
            password= 'test.2022'
        )
        print('[OK] creado superuser...')
    
    def load_users(self):
        for item in range(100):
            user_role = 'asistente'
            if item < 3:
                user_role = 'gestor'
            person_name = self.faker.name()
            new_user = {
                'username': person_name.lower().replace(' ',''),
                'password': ''.join(random.choices(string.ascii_letters, k=18)),
                'first_name': person_name.split(' ')[0],
                'last_name': person_name.split(' ')[1],
                'email': self.faker.email(),
                'role': user_role,
            }
            CustomUserModel.objects.create(**new_user)
        print('[OK] Usuarios Insertados...')
    
    def load_teams(self):
        all_teams = Team.objects.all()
        if len(all_teams):
            print('[Warning] Equipos existentes en la base')
            return None
        
        for item in range(50):
            users_assintants = CustomUserModel.objects.filter(
                role='asistente'
            )
            new_team = {
                'group_number': random.randrange(1,12),
                'manager': users_assintants[random.randrange(1, 95)],
                'warenhouse_assistant': self.faker.name(),                
            }
            Team.objects.create(**new_team)
        print('[OK] Equipos creados...')
    
    def load_products(self):
        file = open('tests/test_data/products.csv', 'r')
        csvreader = csv.reader(file, delimiter=',')
        for line in csvreader:
            my_product = {
                'account_code':line[0],
                'name':line[1],
                'quantity_per_box': line[3] if line[3] else 1,
                'capacity': line[2] if line[2] else None,
                'ean_13_code': line[4],
                'ean_14_code': line[5],
            }
            try:
                Product.objects.create(**my_product)
            except IntegrityError as e:
                pass
        print('[OK] lista de productos completa...')

    def load_warenhouses(self):
        file = open('tests/test_data/warenhouses.csv', 'r')
        csvreader = csv.reader(file, delimiter=',')
        for line in csvreader:
            new_warenhouse = {
                'id_warenhouse_number': line[0],
                'name': line[1],
                'owner': line[2],
            }
            try:
                Warenhouse.objects.create(**new_warenhouse)
            except IntegrityError as e:
                pass
        print('[OK] Bodegas Cargadas...')
    
    def load_sap_migrations(self):

        for item in range(5):
            migration = SapMigration()
            migration.save()      

        print('[OK] Migraciones SAP cargadas...')
        all_sap_migrations = SapMigration.objects.all()
        all_products = Product.objects.all()
        companies = [
            'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.',
            'CORPORACIÓN PLUSBRAND DEL ECUADOR CIA LTDA',
            'IMNAC IMPORTADORA NACIONAL CIA LTDA',
            'PANIAGUA S.A.',
            'REV ECUADOR S.A',
            'SERVMULTIMARC CIA LTDA',
            'VIDINTERNACIONAL S.A.',
            'VINOS Y ESPIRITUOSOS DEL LITORAL VINLITORAL S.A.',
            'VINOS Y ESPIRITUOSOS VINESA S.A.'
        ]
        id_warenhouse = [1, 10, 11, 13, 14, 15, 2, 3, 4, 5, 6, 7, 9, 93]
        warenhouse_name = [
            '10 DE AGOSTO',
            'MAL ESTADO',
            'CARCELEN',
            'CONSIGNACION',
            'CONSIGNACION4',
            'GENERAL',
            'CONTROL DE CALIDAD',
        ]

        for migration in all_sap_migrations:
            for product in all_products:
                on_hand = random.randint(-1,300000)
                on_order = random.randint(-1, 2800)
                is_commited = random.randint(-1, 1500)

                migration_detail = {
                    'id_sap_migration': migration,
                    'account_code':product.account_code,
                    'company_name': random.choice(companies),
                    'name': product.name,
                    'warenhouse_code': random.choice(id_warenhouse),
                    'warenhouse_name': random.choice(warenhouse_name),
                    'on_hand': on_hand,
                    'on_order': on_order,
                    'is_commited': is_commited,
                    'avaliable': (on_hand + on_order - is_commited)
                }
                if random.choice([False,False,False,True,False,False,False]):
                    try:
                        SapMigrationDetail.objects.create(**migration_detail)
                    except IntegrityError as e:
                        pass
        print('[OK] Detalle Migraciones realizadas...')

print('---> START LOAD DATA <---')
loadData = LoadTestData()
loadData.create_super_user()
loadData.load_users()
loadData.load_teams()
loadData.load_products()
loadData.load_warenhouses()
loadData.load_sap_migrations()
print('---> END TASK <---')