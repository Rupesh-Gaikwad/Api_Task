from rest_framework import authentication
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from myAPIs.serializers import UserSerializer, LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#User registration api view
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
            return Response({'message':f'{username} you have been registered successfully.'})
        return Response(serializer.errors)

    
#This view class was created just for demo purpose to check generated token works or not.
# class TestTokenView(ListAPIView):
#      queryset = User.objects.all()
#      serializer_class = UserSerializer
#      authentication_classes = [TokenAuthentication,]
#      permission_classes = [IsAuthenticated,]
