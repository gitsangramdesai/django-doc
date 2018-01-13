from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)


class Review(models.Model):
    product = models.ForeignKey(Product,
                                related_name='reviews',
                                on_delete=models.CASCADE
                                )
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE
                                   )

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)