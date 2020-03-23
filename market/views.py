from django.shortcuts import render
from rest_framework import generics
from .models import Hub
from .serializers import HubSerializer

class ListCreateHubView(generics.ListCreateAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer