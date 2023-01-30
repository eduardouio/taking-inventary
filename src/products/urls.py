from django.urls import path
from products.views import UpdateProductCV, ProductList, ProductDetailView, APIProductDetail

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name="list-product"),
    path('update/', UpdateProductCV.as_view(), name="ajax-product-update"),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name="prouduct-detail"),
    path('api/detail/product/<str:id_product>/migration/<int:id_migration>', APIProductDetail.as_view(),
         name="api-prouduct-detail"),
]
