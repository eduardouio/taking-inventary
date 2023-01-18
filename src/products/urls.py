from django.urls import path
from products.views import UpdateProductCV, ProductDetailTP

app_name = 'products'

urlpatterns = [
    path('update/', UpdateProductCV.as_view(), name="ajax-product-update"),
    path('detail/<int:pk>/', ProductDetailTP.as_view(), name="product-detail"),
]

