from rest_framework import serializers
from .models import User, MerchProfile

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', 'last_name', 'username', 'email', 'password', 'groups']

class MerchProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchProfile
        fields = '__all__'