from django.db import models

# Create your models here.


class Query(models.Model):
    table = models.CharField(max_length=100)
    node = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    truncate = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    weight = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
