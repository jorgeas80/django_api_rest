from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'


'''
Métodos útiles:

* is_valid(self, ...): Dice si los datos son válidos para crear/actualizar una instancia del modelo.
* save(self, ...): Sabe cómo crear o actualizar un modelo.
* create(self, validated_data, ..): Sabe cómo crear la instancia. Se puede sobreescribir para poder personalizar la tarea de creación.
* update(self, instance, validated_data, ..): Sabe cómo actualizar la instancia. Se puede sobreescribir para poder personalizar la tarea de actualización.
'''