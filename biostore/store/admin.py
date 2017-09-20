# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product
from .models import ProductType
from .models import Category

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Category)
