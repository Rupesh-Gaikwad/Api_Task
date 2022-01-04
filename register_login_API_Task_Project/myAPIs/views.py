from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from myAPIs.serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
# Create your views here.

class RegistrationAPI(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            user = User(username=username, email=email)
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'message':'New user registered successfully.'})
        return Response(serializer.errors)

class LoginAPI(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        pass
