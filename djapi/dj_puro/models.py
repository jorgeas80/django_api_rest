from django.db import models

from .mixins import Timestampable, Publishable, Permalinkable, Activable, Showable

# Create your models here.
class Category(Activable, Showable):
    def __str__(self):
        return '{} - {} ({})'.format(
            self.name, 
            self.description,
            'activa' if self.active else 'inactiva')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class SubCategory(Activable, Showable):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} ({})'.format(
            self.name, 
            self.description,
            'activa' if self.active else 'inactiva')

    class Meta:
        verbose_name = 'Subcategoría'
        verbose_name_plural = 'Subcategorías'


class Product(Timestampable, Publishable, Permalinkable, Showable, Activable):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        return '{} - {} ({}) - {} - Actualizado en {}{}'.format(
            self.name, 
            self.description,
            'activo' if self.active else 'inactivo',
            self.slug if self.slug else 'Sin url',
            self.modified_date,
            ' - Publicado en {}.'.format(self.publish_date) if self.publish_date else '.')
