from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.authtoken.models import Token


from .models import User
from .serializers import LoginSerializer, SignupSerializer

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        user = authenticate(username=request.data['email'], password=request.data['password'])
        if user is not None:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"token": None, "message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class SignupView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ForgotPasswordEmail(APIView):
    '''
    Send email with link to reset password
    '''
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            user = User.objects.get(email=request.data['email'])
            token = Token.objects.get(user=user)
        except:
            return Response("You are not a registered user", status=status.HTTP_404_NOT_FOUND)
        
        send_mail(
            subject="Did you forget your password?", 
            message="Please use the below link to reset your password \n\n" + str(settings.DOMAIN_NAME) + "/forgot-password/" + str(token), 
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=[request.data['email']]
        )
        #test will be replaced with appropriate frontend url which will provide a form with new password
        #send token in message to identify user after they've filled the form
        #reset password and token after form submit
        return Response({}, status=status.HTTP_200_OK)

class ForgotPasswordReset(APIView):
    '''
    Reset password from token (obtained through the link in forgot-password-email)
    '''
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        token = Token.objects.filter(key=request.data['token'])
        if token.exists():
            token = token.first()
            user = token.user
            user.set_password(request.data['new_password'])
            user.save()
            token.delete()
            token = Token.objects.create(user=user)
            return Response({'success':True, 'message': 'Successfully changed password', 'token': token.key}, status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Could not password, invalid token'}, status.HTTP_400_BAD_REQUEST)
