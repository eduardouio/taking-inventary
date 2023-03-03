import json
from products.models import Product
from accounts.models.CustomUserModel import CustomUserModel
from django.db import IntegrityError


class SeedData():
    """./manage.py shell < tests/test_data/seed.py"""

    def create_super_user(self):
        CustomUserModel.objects.create_superuser(
            username='admin',
            password='changePassword.2023'
        )
        print('[OK] Admin Created...')

    def load_users(self):
        users_file = open('tests/test_data/users.json')
        users = json.loads(users_file.read())['users']

        for user in users:
            user['password'] = '1234.abc'
            try:
                CustomUserModel.objects.create(**user)
            except:
                print(f"[ERROR] {user['username']} it already exist")
        print('[OK] Users Loaded...')

    def load_products(self):
        products_file = open('tests/test_data/products.json', 'r')
        products = json.loads(products_file.read())['products']

        for product in products:
            try:
                Product.objects.create(**product)
            except IntegrityError as e:
                print(f"[ERROR] => {product['name']} {e.__str__()}")
        print('[OK] products created...')

    def unifyPassworwds(self):
        print('unifying passwords users...')
        all_users = CustomUserModel.objects.all()
        for user in all_users:
            if user.username != 'eduardo' and user.username != 'AnonymousUser':
                user.set_password('1234.abc')
                user.save()
                print(f"{user.username} updated")


print('---> START LOAD SEED DATA <---')
my_seed = SeedData()
my_seed.create_super_user()
my_seed.load_users()
my_seed.load_products()
print('---> END TASK <---')
