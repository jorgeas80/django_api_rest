from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User, Category, SubCategory, Product

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
