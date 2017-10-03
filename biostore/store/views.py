# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Category
from django.http import HttpResponse
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.

class ListCreateProduct(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class RetriveUpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ListCreateCategory(generics.ListCreateAPIView):
        queryset = models.Category.objects.all()
        serializer_class = serializers.CategorySerializer

class RetriveUpdateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
        queryset = models.Category.objects.all()
        serializer_class = serializers.CategorySerializer

class ListCreateProductType(generics.ListCreateAPIView):
    queryset = models.ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer

class RetriveUpdateDestroyProductType(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer

class ListOrdersToProducer(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class RetrieveOrderByConsumer(generics.RetrieveAPIView):
    serializer_class = serializers.OrderSerializer

    def get_object(self):
        return models.Order.objects.filter(consumer_id=self.kwargs.get('consumer_pk')).last()
