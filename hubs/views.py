from django.shortcuts import get_object_or_404
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

    def get_queryset(self):
        hub = get_object_or_404(Hub, hub_id = self.kwargs.get('hub_id'))
        return Merchant.objects.filter(hub_id = hub)

class HubListView(generics.ListAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer