from django.urls import path
from .views import *

urlpatterns = [
    path('v1/products/', ProductListBasic.as_view(), name='product_list_basic'),
    path('v1/products/<int:pk>', ProductDetailBasic.as_view(), name='product_detail_basic'),
    path('v2/products/', ProductList.as_view(), name='product_list'),
    path('v2/products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('v2/categories/', CategorySave.as_view(),name='category_save'),
    path('v2/subcategories/', SubCategorySave.as_view(),name='subcategory_save')
]
