# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ProductType
from .models import Category
from .models import PaymentType
from .models import Payment
from .models import Order
from .models import  Consumer
from .models import Order_Item
from .models import Producer
from .models import ProducerOffer
from .models import AdminOffer
from .models import Notification

# Register your models here.
class ProducerDisplay(admin.ModelAdmin):
    list_display = ('uid','name','last_name')
    search_fields = ['name']
class NotificationDisplay(admin.ModelAdmin):
    list_display = ('title', 'text', 'img')
    search_fields = ['title']

class OrderDisplay(admin.ModelAdmin):
    list_display = ('consumer', 'shipping_address', 'delivery_at')
    search_fields = ['consumer']
class ConsumerDisplay(admin.ModelAdmin):
    list_display = ('name', 'email', 'last_name')
    search_fields = ['name']

class OrderItemDisplay(admin.ModelAdmin):
    list_display = ('count', 'offer', 'state')
    search_fields = ['state']

admin.site.register(ProductType)
admin.site.register(Category)
admin.site.register(PaymentType)
admin.site.register(Payment)
admin.site.register(Order, OrderDisplay)
admin.site.register(Consumer, ConsumerDisplay)
admin.site.register(Order_Item, OrderItemDisplay)
admin.site.register(Producer, ProducerDisplay)
admin.site.register(ProducerOffer)
admin.site.register(AdminOffer)
admin.site.register(Notification, NotificationDisplay)
