from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('v1/products/', ProductListBasic.as_view(), name='product_list_basic'),
    path('v1/products/<int:pk>', ProductDetailBasic.as_view(), name='product_detail_basic'),
    path('v2/categories/', CategoryList.as_view(),name='category_list'),
    path('v2/categories/<int:pk>', CategoryDetail.as_view(),name='category_detail'),
    path('v2/categories/<int:pk>/subcategories', SubCategoryList.as_view(), name='subcategory_list'),
    path('v3/users/', UserCreate.as_view(), name='user_create'),
    path('v3/login/', LoginView.as_view(), name='login'),
    path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),
]

router = DefaultRouter()
router.register('v2/products', ProductViewSet, base_name='products')
urlpatterns += router.urls
