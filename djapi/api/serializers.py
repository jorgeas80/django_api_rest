from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    # Check https://www.django-rest-framework.org/api-guide/validators/#currentuserdefault
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Category
        fields= '__all__'
 
class SubCategorySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = SubCategory
        fields= '__all__'


class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user