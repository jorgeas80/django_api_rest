from django.db import models
from django.http import JsonResponse

# Create your models here.
class Permalinkable(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Activable(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Showable(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    class Meta:
        abstract = True
