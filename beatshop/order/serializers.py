from rest_framework import serializers
from .models import Order, OrderItem
from shop.serializers import ProductSerializer


class CustomersOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = [
            'price',
            'product',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'price',
            'product',
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'stripe_token',
            'items',
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
    

class CustomersOrderSerializer(serializers.ModelSerializer):
    items = CustomersOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'stripe_token',
            'items',
            'paid_amount'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order