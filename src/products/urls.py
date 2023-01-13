from django.urls import path
from products.views import updateProduct

app_name = 'products'

urlpatterns = [
    path('update/', updateProduct, name="accounts-create-team"),
]

