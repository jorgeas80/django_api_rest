from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Category, SubCategory, Product

# Create your views here.
class CategoryListView(ListView):
    model = Category


class SubCategoryListView(ListView):
    model = SubCategory


class ProductListView(ListView):
    model = Product
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CategoryDetailView(DetailView):
    model = Category


class SubCategoryDetailView(DetailView):
    model = SubCategory


class ProductDetailView(DetailView):
    model = Product
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

