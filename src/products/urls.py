from django.urls import path
from products.views import updateProduct, ProductDetailTP

app_name = 'products'

urlpatterns = [
    path('update/', updateProduct, name="accounts-create-team"),
    path('detail/<int:pk>/', ProductDetailTP.as_view(), name="product-detail"),
]

