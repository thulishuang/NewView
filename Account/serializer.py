from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('username', 'password')


class AuthenticationSerializer(serializers.ModelSerializer):
    error_code = serializers.IntegerField(default=0)