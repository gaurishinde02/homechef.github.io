from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# We will create a class(model) for our table Books
# The models.cascade for author field states that if a User is deleted, then its respective Book should also be deleted

# The dunder str method [double underscore method]
# These are also called magic/special methods
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_published = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#


class Recipe(models.Model):
    recipename = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=500)
    calories = models.CharField(max_length=200)
    def __str__(self):
        return self.recipename


class Ingredient(models.Model):
    ingredientname = models.CharField(max_length=50)
