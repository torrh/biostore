# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from .models import Category, Consumer
from django.http import HttpResponse, JsonResponse
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

@csrf_exempt
def register_consumer(request):
    if request.method == 'POST':
        uid = request.POST.get('cedula')
        name = request.POST.get('name')
        email = request.POST.get('email')
        lastname = request.POST.get('lastname')
        password= request.POST.get('password')
        address=request.POST.get('address')

        phone_number= request.POST.get('phone_number')
        new_consumer = Consumer.objects.create(uid=uid,name=name,last_name=lastname,email=email,address= address,password=password,
                                               phone_number=phone_number)
        new_consumer.save();

@csrf_exempt
def login(request):
    mensaje='error'
    if request.method =='POST':
        email = request.POST.get('email')
        password= request.POST.get('password')
        consumer_bd = Consumer.objects.get(email=email)
        if consumer_bd.password == password:
            mensaje='ok'
    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def consumer_details(request,email):
    mensaje="Consumer not found"
    if request.method=='GET':

        consumer_bd = Consumer.objects.get(email=email)

        if consumer_bd.email ==  email:
            data = {'name':consumer_bd.name,
               'last_name':consumer_bd.last_name,
               'email':email,
               'address':consumer_bd.address,
               'phone_number':consumer_bd.phone_number
               }
        return JsonResponse({"data":data})
    return JsonResponse({"error":mensaje })

class ListOrdersToProducer(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class RetrieveOrderByConsumer(generics.RetrieveAPIView):
    serializer_class = serializers.OrderSerializer

    def get_object(self):
        return models.Order.objects.filter(consumer_id=self.kwargs.get('consumer_pk')).last()









