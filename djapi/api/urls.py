from django.urls import path
from .views import *

urlpatterns = [
    path('v1/products/', ProductListBasic.as_view(), name='product_list_basic'),
    path('v1/products/<int:pk>', ProductDetailBasic.as_view(), name='product_detail_basic'),
    path('v2/products/', ProductList.as_view(), name='product_list'),
    path('v2/products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('v2/categories/', CategoryList.as_view(),name='category_list'),
    path('v2/categories/<int:pk>', CategoryDetail.as_view(),name='category_detail'),
    path('v2/categories/<int:pk>/subcategories', SubCategoryList.as_view(), name='subcategory_list')
]
