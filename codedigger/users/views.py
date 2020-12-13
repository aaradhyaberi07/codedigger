from django.shortcuts import render
from rest_framework import generics,status,permissions,views
from .serializers import RegisterSerializer,ProfileSerializer,EmailVerificationSerializer,LoginSerializer,RequestPasswordResetEmailSeriliazer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Profile
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings  
import jwt
from .permissions import IsOwner
from rest_framework.generics import RetrieveAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.generics import UpdateAPIView,ListAPIView
from .renderers import UserRenderer





class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = [UserRenderer]

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data = user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain

        relative_link = reverse('email-verify')


        absurl = 'https://' + current_site + relative_link + "?token=" + str(token)
        email_body = 'Hi' + user.username + '. Use link below to verify your email \n' + absurl
        data = {'email_body' : email_body,'email_subject' : 'Verify your email','to_email' : user.email}
        Util.send_email(data)
        return Response(user_data,status = status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer
    
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email' : 'Successfully activated'},status = status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'email' : 'Activation link expired'},status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'email' : 'Invalid token, Request New One'},status = status.HTTP_400_BAD_REQUEST)


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        return Response(serializer.data,status = status.HTTP_200_OK)




class ProfileGetView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = Profile.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)



class ProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = Profile.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSeriliazer

    def post(self,request):
        serializer = self.serializer_class(data = request.data)



