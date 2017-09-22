# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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