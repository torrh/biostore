# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=1000)

class Category(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=1000)

class Product(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    unit_price = models.FloatField()
    count = models.IntegerField()
    unit_type = models.CharField(max_length=255)
    available_at = models.DateField()
    productType = models.ForeignKey(ProductType)
    category = models.ForeignKey(Category)