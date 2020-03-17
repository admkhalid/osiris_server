from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import generics
from .models import Hub, Merchant, Product
from .serializers import (MerchantSerializer, HubSerializer, ProductSerializer,
                        HubListSerializer, MerchantListSerializer, ProductListSerializer)
from rest_framework import permissions
from . import permissions as cust_permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class MerchantCreateView(generics.CreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    def post(self, request, *args, **kwargs):
        Res = super().post(request, *args, **kwargs)
        token = Token.objects.get(user=User.objects.get(id=Res.data['id'])).key
        Res.data['token'] = token
        return Res

class MerchantListView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantListSerializer

    # class Meta:
    #     fields = ['first-name', 'last-name', 'phone']

    def get_queryset(self):
        hub = get_object_or_404(Hub, hub_id = self.kwargs.get('hub_id'))
        return Merchant.objects.filter(hub_id = hub)

class MerchantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [cust_permissions.IsOwnerOrReadOnly]

class HubListView(generics.ListAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubListSerializer

class HubDetailView(generics.RetrieveAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    permission_classes = [cust_permissions.IsAdminUserOrReadOnly]

##List products specific to a merchant
class MerchantProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        merchant = get_object_or_404(Merchant, id=self.kwargs.get('pk'))
        return Product.objects.filter(merchant = merchant)

#List all products available in a HUB

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        merchants = get_list_or_404(Merchant, hub_id = self.kwargs.get('hub_id'))
        return Product.objects.filter(merchant__in = merchants)
        ## add __in to the attribute name if your filter parameter is a list of some stuff

    def perform_create(self, serializer):
        serializer.save(merchant=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [cust_permissions.IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        m = Merchant.objects.get(username=self.request.user.username)
        serializer.save(merchant=m)

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        m = Merchant.objects.get(username=self.request.user.username)
        serializer.save(merchant=m)

@api_view(['POST'])
def merchantLogin(request, *args, **kwargs):
    m = Merchant.objects.get(username=request.data['username'])
    Token.objects.create(user=m)
    res = {}
    # res['token'] = Token.objects.get(user=User.objects.get(username=request.data['username'])
    u = User.objects.get(username=request.data['username'])
    res['token'] = Token.objects.get(user=u).key
    return Response(res)