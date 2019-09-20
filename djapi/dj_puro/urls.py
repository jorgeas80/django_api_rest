from django.urls import path
from .views import CategoryDetailView, CategoryListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
]
