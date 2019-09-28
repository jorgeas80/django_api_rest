from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Curso Django REST API con DRF",
      default_version='v1',
      description="Documentación para el curso de Django REST API usando DRF",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/products/', ProductListBasic.as_view(), name='product_list_basic'),
    path('v1/products/<int:pk>', ProductDetailBasic.as_view(), name='product_detail_basic'),
    path('v2/categories/', CategoryList.as_view(),name='category_list'),
    path('v2/categories/<int:pk>', CategoryDetail.as_view(),name='category_detail'),
    path('v2/categories/<int:pk>/subcategories', SubCategoryList.as_view(), name='subcategory_list'),
    path('v3/users/', UserCreate.as_view(), name='user_create'),
    path('v3/login/', LoginView.as_view(), name='login'),
    path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

router = DefaultRouter()
router.register('v2/products', ProductViewSet, base_name='products')
urlpatterns += router.urls
