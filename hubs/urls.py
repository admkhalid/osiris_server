from django.contrib import admin
from django.urls import path, include
from .views import MerchantCreateView, MerchantListView, HubListView

urlpatterns = [
    path('create-merch/', MerchantCreateView.as_view()),
    path('list-merch/', MerchantListView.as_view()),
    path('list-hub/', HubListView.as_view()),
]