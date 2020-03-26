from django.contrib import admin
from django.urls import path, include
from .views import (CustomerCreateView, CustomerDetailView, CartItemCreateView, CartItemListView, orderItems,
                    OrderDetailSerializer)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', CustomerCreateView.as_view()),
    path('detail/<int:pk>/', CustomerDetailView.as_view(), name='cust-detail'),
    path('cart-post/', CartItemCreateView.as_view()),
    path('cart-list/', CartItemListView.as_view()),
    path('order/', orderItems),
    path('order-detail/', OrderDetailSerializer.as_view()),
]