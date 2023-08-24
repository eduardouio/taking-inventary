import pytest
from django.contrib.auth import get_user_model as UserModel
from products.models import Product
import requests


@pytest.mark.django_db
class TestImagesUrls:
    
    def client(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user)
        return client

    def test_get_image_front(self, client):
        errors = []
        products = Product.objects.all()
        for product in products:
            if product.image_front:
                url = 'http://localhost:8000' +  product.image_front.url
                response = requests.get(url)
                if response.status_code != 200:
                    errors.append('{}:{}:{}'.format(
                        product.account_code,
                        product.name,
                        product.image_front
                    ))

        assert len(errors) == 0

        
        