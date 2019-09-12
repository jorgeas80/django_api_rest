from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Category

# Create your views here.
class CategoryListView(ListView):
    model = Category
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
