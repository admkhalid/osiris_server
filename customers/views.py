from django.shortcuts import render
from .models import Customer, CartItem
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from hubs.permissions import IsOwnerOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import CartItemSerializer, OrderSerializer
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        Res = super().post(request, *args, **kwargs)
        token = Token.objects.get(user=User.objects.get(id=Res.data['id'])).key
        Res.data['token'] = token
        return Res

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsOwnerOrReadOnly]

@api_view(['POST'])
def custLogin(request, *args, **kwargs):
    m = Customer.objects.get(username=request.data['username'])
    Token.objects.create(user=m)
    res = {}
    # res['token'] = Token.objects.get(user=User.objects.get(username=request.data['username'])
    u = User.objects.get(username=request.data['username'])
    res['token'] = Token.objects.get(user=u).key
    res['url'] = reverse('merch-detail', kwargs={'pk': m.id})
    return Response(res)

# @csrf_exempt
# @api_view(['GET', 'POST', 'PUT'])
# def cartView(request):
#     key = request.auth.key
#     token = Token.objects.get(key=key)
#     customer = Customer.objects.get(username=token.user.username)

#     if request.method == 'POST':
#         serializer = CartItemSerializer()

#     return HttpResponse(content=b'shit')

class CartItemCreateView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        c = Customer.objects.get(username=self.request.user.username)
        serializer.save(customer=c)

class CartItemListView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     s = []
    #     for i in self.queryset:
    #         if i.item.

    def get_queryset(self):
        # customer = get_object_or_404(CartItem, customer = self.request.user.id)
        cust = Customer.objects.get(id=self.request.user.id)
        return CartItem.objects.filter(customer = cust)

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # customer = get_object_or_404(CartItem, customer = self.request.user.id)
        cust = Customer.objects.get(id=self.request.user.id)
        return CartItem.objects.filter(customer = cust)

class OrderDetailSerializer(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cust = Customer.objects.get(id=self.request.user.id)
        return CartItem.objects.filter(customer = cust)

@api_view(['GET'])
def orderItems(request, *args, **kwargs):
    cust = Customer.objects.get(id=request.user.id)
    items = CartItem.objects.filter(customer=cust)

    for i in items:
        i.ordered = True
        i.save()

    return Response(data={"ordered": "True"})