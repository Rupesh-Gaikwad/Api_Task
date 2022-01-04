from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password','confirm_password')

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        if username == None or email == None:
            raise serializers.ValidationError('Username and email is compulsory.')
        password1 = data.get('password')
        password2 = data.get('confirm_password')
        if password1 != password2:
            raise serializers.ValidationError('Passwords Must Match...')
        return data

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
