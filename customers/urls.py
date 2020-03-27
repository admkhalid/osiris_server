from django.contrib import admin
from django.urls import path, include
from .views import (CustomerCreateView, CustomerDetailView, CartItemCreateView, CartItemListView, orderItems,
                    OrderDetailSerializer, custLogin, CartItemDetailView)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', CustomerCreateView.as_view()),
    path('detail/<int:pk>/', CustomerDetailView.as_view(), name='cust-detail'),
    path('login/', custLogin),
    path('cart-post/', CartItemCreateView.as_view()),
    path('cart-item/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('cart-list/', CartItemListView.as_view()),
    path('order/', orderItems),
    path('order-detail/', OrderDetailSerializer.as_view()),
]