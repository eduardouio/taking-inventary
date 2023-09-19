import pytest
from django.shortcuts import reverse
from django.contrib.auth import get_user_model as UserModel


@pytest.mark.django_db
class TestProductStockImgs():

    @pytest.fixture
    def url(self):
        return reverse('products:list-products-imgs')
    
    @pytest.fixture
    def client(self, client):
        user = UserModel().objects.get(username='evillota')
        client.force_login(user)
        return client

    
    def test_get_queryset(self, client, url):
        response = client.get(url)
        assert response.status_code == 200
        assert response.template_name[0] == 'products/stock-imgs.html'
        

