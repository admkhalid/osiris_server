from django.contrib import admin
from django.urls import path, include
from .views import (
    MerchantCreateView, MerchantListView, HubListView, HubDetailView, ProductListView,
    ProductDetailView, ProductCreateView)

urlpatterns = [
    path('', HubListView.as_view()),
    path('create-merch/', MerchantCreateView.as_view()),
    path('<str:pk>/', HubDetailView.as_view(), name='hub-detail'),
    path('<str:hub_id>/merch/', MerchantListView.as_view()),
    path('<str:hub_id>/products/', ProductListView.as_view()),
    path('<str:hub_id>/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<str:hub_id>/products/create/', ProductCreateView.as_view()),
]