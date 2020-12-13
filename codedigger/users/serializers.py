from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import User,Profile
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed,ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes,smart_str,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from  rest_framework_simplejwt.tokens import RefreshToken,TokenError




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password']
         
    def validate(self,attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length = 555)
    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255,min_length=3,read_only=True)
    password = serializers.CharField(max_length = 68,min_length = 6,write_only=True)
    username = serializers.CharField(max_length = 68)
    tokens = serializers.SerializerMethodField()


    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    
    class Meta:
        model = User
        fields = ['id','username','email','password','tokens']

    def validate(self,attrs):
        username =  attrs.get('username','')
        password =  attrs.get('password','')
        user_obj_email = User.objects.filter(email=username).first()
        user_obj_username = User.objects.filter(username=username).first()
        if user_obj_email:
            # if user_obj_email.is_authenticated:
            #     raise AuthenticationFailed('Already Logged In')
            user = auth.authenticate(username = user_obj_email.username,password=password)
            if user_obj_email.auth_provider != 'email':
                raise AuthenticationFailed(
                    detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
            if not user:
                raise AuthenticationFailed('Invalid credentials. Try again')
            if not user.is_active:
                raise AuthenticationFailed('Account disabled. contact admin')
            if not user.is_verified:
                raise AuthenticationFailed('Email is not verified')
            return {
                'email' : user.email,
                'username' : user.username,
                'tokens': user.tokens
            }
            return super().validate(attrs)
        if user_obj_username:
            # if user_obj_username.is_authenticated:
            #     raise AuthenticationFailed('Already Logged In')
            user = auth.authenticate(username = username,password=password)
            if not user:
                raise AuthenticationFailed('Invalid credentials. Try again')
            if not user.is_active:
                raise AuthenticationFailed('Account disabled. contact admin')
            if not user.is_verified:
                raise AuthenticationFailed('Email is not verified')
            return {
                'email' : user.email,
                'username' : user.username,
                'tokens': user.tokens
            }
            return super().validate(attrs)
        raise AuthenticationFailed('Invalid credentials. Try again')
        

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[required])
    codeforces = serializers.CharField(validators=[required])
    class Meta:
        model = Profile
        fields = ['id','name','codeforces','codechef','atcoder','spoj','uva_handle','uva_id']


    
    


class RequestPasswordResetEmailSeriliazer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']


    
