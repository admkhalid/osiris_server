from rest_framework import serializers
from .models import Merchant, Product, Hub

class HubSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='hub-detail', format='html')

    class Meta:
        model = Hub
        fields = ['hub_id', 'url', 'x_co_ord', 'y_co_ord', 'area', 'area_code']

class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, style = {'input_type': 'password'}) #FOR USER CREATION PURPOSE
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    # products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)
    class Meta:
        model = Merchant
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone', 'hub', 'products']
    
    def create(self, validated_data):
        merchant = super(MerchantSerializer, self).create(validated_data)
        merchant.set_password(validated_data['password'])
        merchant.save()
        return merchant

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    merchant = serializers.ReadOnlyField(source='merchant.username')
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    class Meta:
        model = Product
        fields = ['id', 'merchant', 'name', 'family', 'image', 'avail_quantity', 'rate']