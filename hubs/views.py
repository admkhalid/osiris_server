from django.shortcuts import render
from rest_framework import generics
from .models import Hub, Merchant, Product
from .serializers import MerchantSerializer, HubSerializer

# Create your views here.

class MerchantCreateView(generics.CreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer 

class MerchantListView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    class Meta:
        fields = ['first-name', 'last-name', 'phone']

class HubListView(generics.ListAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer