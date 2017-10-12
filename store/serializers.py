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

class ProducerOfferSerializer(serializers.ModelSerializer):

    productType = ProductTypeSerializer(read_only=True)

    class Meta:
        fields = (
            'modifiable',
            'stage',
            'unit_price',
            'count',
            'unit_type',
            'available_at',
            'productType',
            'producer'
        )
        model = models.ProducerOffer

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

    productType = ProductTypeSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        fields = (
            'count',
            'productType',
            'order'
        )
        model = models.Order_Item
