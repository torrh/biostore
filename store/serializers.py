from rest_framework import serializers

from . import models

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description',
            'url',
        )
        model = models.ProductType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'url',
        )
        model = models.Category

class ProductSerializer(serializers.ModelSerializer):

    productType = ProductTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True);

    class Meta:
        fields = (
            'create_at',
            'unit_price',
            'count',
            'unit_type',
            'available_at',
            'productType',
            'category'
        )
        model = models.Product