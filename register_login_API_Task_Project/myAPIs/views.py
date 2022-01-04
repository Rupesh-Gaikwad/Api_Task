from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from myAPIs.serializers import UserSerializer
# Create your views here.

class RegistrationAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPI(CreateAPIView):
    pass
