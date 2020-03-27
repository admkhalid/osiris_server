from rest_framework import serializers
from .models import Customer, CartItem

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, style = {'input_type': 'password'}) #FOR USER CREATION PURPOSE
    url = serializers.HyperlinkedIdentityField(view_name='cust-detail')

    class Meta:
        model = Customer
        fields = ['id', 'url', 'first_name', 'last_name', 'username', 'profile_pic', 'email', 'password', 'phone', 'address']
    
    def create(self, validated_data):
        customer = super(CustomerSerializer, self).create(validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    url = serializers.HyperlinkedIdentityField(view_name='cart-item-detail')

    class Meta:
        model = CartItem
        fields = ['id', 'url', 'customer', 'item', 'quantity']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    url = url = serializers.HyperlinkedIdentityField(view_name='order-detail')

    class Meta:
        model = CartItem
        fields = ['item', 'url', 'quantity', 'ordered', 'processed']