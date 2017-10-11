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

class ProductOrderSerializer(serializers.ModelSerializer):

    productType = ProductTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True);

    class Meta:
        fields = (
            'unit_type',
            'productType',
            'category',
            'producer'
        )
        model = models.Product

class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title'
        )
        model = models.PaymentType

class PaymentSerializer(serializers.ModelSerializer):

    paymentType = PaymentTypeSerializer(read_only=True)

    class Meta:
        fields = (
            'amount',
            'state',
            'paymentType'
        )
        model = models.Payment

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'delivery_at',
            'shipping_address',
        )
        model = models.Order

class OrderItemSerializer(serializers.ModelSerializer):

    product = ProductOrderSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        fields = (
            'count',
            'product',
            'order'
        )
        model = models.Order_Item


class ProductCategorySerializer(serializers.ModelSerializer):

    productType = ProductTypeSerializer(read_only=True)
    category =  CategorySerializer(read_only=True)

    class Meta:
        fields = (
            'unit_type',
            'productType',
            'category',
            'unit_price'
        )
        model= models.Product
