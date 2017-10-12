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

class Producer(models.Model):
    uid = models.FloatField()
    email = models.EmailField()
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone_number = models.CharField(max_length=255)

class Administrator(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

class ProducerOffer(models.Model):
    create_at = models.BigIntegerField()
    modifiable =  models.BooleanField()
    stage = models.TextField()
    unit_price = models.FloatField()
    count = models.IntegerField()
    unit_type = models.CharField(max_length=255)
    available_at = models.BigIntegerField()
    productType = models.ForeignKey(ProductType)
    producer = models.ForeignKey(Producer)

class Consumer(models.Model):
    uid = models.FloatField()
    email = models.EmailField()
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=50, default="1234")
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

class PaymentType(models.Model):
    title = models.CharField(max_length=255)

class Payment(models.Model):
    amount = models.FloatField()
    state = models.BooleanField()
    paymentType = models.ForeignKey(PaymentType)

class Order(models.Model):
    create_at = models.BigIntegerField()
    delivery_at = models.BigIntegerField()
    shipping_address = models.CharField(max_length=255)
    consumer = models.ForeignKey(Consumer)
    payment = models.ForeignKey(Payment)

class Order_Item(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(ProductType)
    order = models.ForeignKey(Order, default=1)