from rest_framework import serializers
from .models import Merchant, Product, Hub

class MerchantSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style = {'input_type': 'password'}) #FOR USER CREATION PURPOSE
    # products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Merchant
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone', 'hub']
    
    def create(self, validated_data):
        merchant = super(MerchantSerializer, self).create(validated_data)
        merchant.set_password(validated_data['password'])
        merchant.save()
        return merchant


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ['hub_id', 'x_co_ord', 'y_co_ord', 'area', 'area_code']

class ProductSerializer(serializers.ModelSerializer):
    merchant = serializers.ReadOnlyField(source='merchant.username')

    class Meta:
        model = Product
        fields = ['id', 'merchant', 'name', 'family', 'avail_quantity']