from django.contrib import admin
from django.urls import path, include
from .views import (
    MerchantCreateView, MerchantListView, HubListView, HubDetailView, ProductListView,
    ProductDetailView, ProductCreateView, MerchantDetailView, MerchantProductListView, 
    merchantLogin)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HubListView.as_view()),
    path('<str:pk>/', HubDetailView.as_view(), name='hub-detail'),
    path('<str:hub_id>/merch/', MerchantListView.as_view()),
    path('merch/<int:pk>/', MerchantDetailView.as_view(), name='merch-detail'),
    path('merch/<int:pk>/products/', MerchantProductListView.as_view()),
    path('merch/create/', MerchantCreateView.as_view()),
    path('<str:hub_id>/products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view()),
    path('login/testlogin/', auth_views.LoginView.as_view(template_name = 'hubs/login.html'), name = 'testlogin'),
    path('merch/login/', merchantLogin),
    path('rest-auth/', include('rest_auth.urls')),
]