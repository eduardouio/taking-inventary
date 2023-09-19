from django.urls import path

from products.views import (APIProductDetail, ProductDetailView, ProductList,
                            UpdateProductCV, ProductStockImgs)

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name="list-product"),
    path('update/', UpdateProductCV.as_view(), name="ajax-product-update"),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name="prouduct-detail"),
    path('api/detail/product/<str:id_product>/migration/<int:id_migration>', APIProductDetail.as_view(),name="api-prouduct-detail"),
    path('list-imgs/', ProductStockImgs.as_view(),name="list-products-imgs"),
]

