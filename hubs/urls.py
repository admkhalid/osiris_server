from django.contrib import admin
from django.urls import path, include
from .views import MerchantCreateView, MerchantListView, HubListView, ProductListView

urlpatterns = [
    path('list-hub/', HubListView.as_view()),
    path('create-merch/', MerchantCreateView.as_view()),
    path('list-merch/<str:hub_id>/', MerchantListView.as_view()),
    path('list-products/<str:hub_id>/', ProductListView.as_view()),
]