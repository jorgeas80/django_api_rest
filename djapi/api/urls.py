from django.urls import path
from .views import *

urlpatterns = [
    path('v1/products/', ProductListBasic.as_view(), name='product_list_basic'),
    path('v1/products/<int:pk>', ProductDetailBasic.as_view(), name='product_detail_basic'),
]
