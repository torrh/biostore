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

# Register your models here.
class ProducerDisplay(admin.ModelAdmin):
    list_display = ('uid','name','last_name')
    search_fields = ['name']

admin.site.register(ProductType)
admin.site.register(Category)
admin.site.register(PaymentType)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Consumer)
admin.site.register(Order_Item)
admin.site.register(Producer, ProducerDisplay)
admin.site.register(ProducerOffer)
admin.site.register(AdminOffer)
