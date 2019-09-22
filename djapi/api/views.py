from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer


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
