from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import *


# Basic view, not using generics
class ProductListBasic(APIView):
    def get(self, request):
        prod = Product.objects.all()
        data = ProductSerializer(prod, many=True).data
        return Response(data)


class ProductDetailBasic(APIView):
    def get(self, request, pk):
        prod = get_object_or_404(Product, pk=pk)
        data = ProductSerializer(prod).data
        return Response(data)


# 'Smart' views, using generics
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategorySave(generics.CreateAPIView):
    serializer_class = CategorySerializer


class SubCategorySave(generics.CreateAPIView):
        serializer_class = SubCategorySerializer
