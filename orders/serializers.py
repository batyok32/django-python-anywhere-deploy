# Rest framework
from rest_framework import serializers

# Models
from .models import  Order, OrderItem

# Serializers
from shop.serializers import CouponSerializer, ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    city_display = serializers.CharField(
        source='get_city_display',
        required=False
    )
    total_products=serializers.IntegerField(
        source='get_total_products',
        required=False
    )
    coupon = CouponSerializer(required=False)

    class Meta:
        model = Order
        fields = ('id', 'full_name', 'user', 'email', 'address', 'city','city_display',
            'coupon', 'discount', 'phone_number', 'order_notes', 'created', 'total_shop', 'total_products')
        read_only_fields= ['user', 'created', 'city_display', 'id', 'total_shop','total_products', 'coupon']

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantity')
        read_only_fields= ['order', 'product']

class SecondOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantity')
        read_only_fields= ['order', 'product']