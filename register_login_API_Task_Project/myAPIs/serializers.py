from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password','re_password')

    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('re_password')
        if password1 != password2:
            raise serializers.ValidationError('Passwords Must Match...')
        return data

    def create(self, validated_data):
        user = User( username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        headers = self.get_success_headers(user.data)
        return Response({'Message': 'You have successfully register'}, status=201, headers=headers)