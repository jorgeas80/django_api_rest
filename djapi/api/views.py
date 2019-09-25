from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import Product
from .permissions import IsOwner
from .serializers import *


# Basic view, not using generics
class ProductListBasic(APIView):
    '''Inheriting from APIView is useful if we want full control over
    the behaviour of our view'''
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
class ProductViewSet(viewsets.ModelViewSet):
    '''Inheriting from viewsets.ModelViewSet is useful if we just want
    to enable full CRUD functionality for a model'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class CategoryList(generics.ListCreateAPIView):
    '''Inheriting from generics.* allows more control than inheriting from
    viewsets.ModelViewSet, but less control than inherigin from APIView. 
    For example, is useful if we just want to implement some CRUD
    functionalities, but not all of them (ListCreateAPIView --> POST, GET)'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 
class SubCategoryList(generics.ListCreateAPIView):
    '''Get subcategories of a given category'''
    def get_queryset(self):
        queryset = SubCategory.objects.filter(category_id=self.kwargs['pk'])
        return queryset

    serializer_class = SubCategorySerializer


class UserCreate(generics.CreateAPIView):
    # Override default configuration for views (ask for authenticated user)
    authentication_classes = {}
    permission_classes = {}
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
 
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)