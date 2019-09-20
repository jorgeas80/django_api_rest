from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories2/', category_list_2, name='category_list_2'),
    path('categories/<int:pk>', category_detail, name='category_detail'),
    re_path(r'^categories2/(?P<pk>\d+)$', category_detail_2, name='category_detail_2'),
    re_path(r'^categories3/(?P<pk>\d+)$', category_detail_3, name='category_detail_3'),
]
