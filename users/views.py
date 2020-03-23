from django.shortcuts import render
from rest_framework import generics
from .models import User, MerchProfile
from .serializers import UserDetailSerializer, MerchProfileSerializer

class UserCreateVeiw(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer 

class MerchProfileCreateView(generics.CreateAPIView):
    queryset = MerchProfile.objects.all()
    serializer_class = MerchProfileSerializer