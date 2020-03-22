from django.contrib import admin
from django.urls import path, include
from .views import CustomerCreateView, CustomerDetailView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', CustomerCreateView.as_view()),
    path('detail/<int:pk>/', CustomerDetailView.as_view(), name='cust-detail'),
]