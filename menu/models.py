from django.db import models
from django.utils import timezone

class Menu(models.Model):
    season = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField()
    items = models.ManyToManyField('Item')

    def __str__(self):
        return self.season


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    standard = models.BooleanField(default=False)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
