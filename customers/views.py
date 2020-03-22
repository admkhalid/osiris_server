from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from hubs.permissions import IsOwnerOrReadOnly

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