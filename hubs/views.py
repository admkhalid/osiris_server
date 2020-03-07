from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import generics
from .models import Hub, Merchant, Product
from .serializers import MerchantSerializer, HubSerializer, ProductSerializer

# Create your views here.

class MerchantCreateView(generics.CreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer 

class MerchantListView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    class Meta:
        fields = ['first-name', 'last-name', 'phone']

    def get_queryset(self):
        hub = get_object_or_404(Hub, hub_id = self.kwargs.get('hub_id'))
        return Merchant.objects.filter(hub_id = hub)

class HubListView(generics.ListAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer

##List products specific to a merchant
class MerchantProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        merchant = get_object_or_404(Merchant, username = self.kwargs.get('username'))
        return Product.objects.filter(merchant = merchant)

#List all products available in a HUB

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        merchants = get_list_or_404(Merchant, hub_id = self.kwargs.get('hub_id'))
        return Product.objects.filter(merchant__in = merchants)
        ## add __in to the attribute name if your filter parameter is a list of some stuff