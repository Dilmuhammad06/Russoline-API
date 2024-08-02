from rest_framework import serializers
from django.contrib.auth import authenticate

from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','image']


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=50,write_only=True)
    username = serializers.CharField(max_length=255)

    def validate(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username,password=password)

        if user is None:
            raise ValidationError({'status':False,'message':'Hatolik'})
        return user

    def to_representation(self, user):
        refresh = RefreshToken.for_user(user)

        data = {
            'email': user.email,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    def __init__(self,*args,**kwargs):
        super(RegisterSerializer,self).__init__(*args,**kwargs)
        self.fields['confirm_password'] = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','password','email']

    def validate(self,data):
        password = data.get('password')
        password_confirm = data.get('confirm_password')

        if password != password_confirm:
            result = {
                "status":False,
                "message":"Passwords dont match"
            }
            raise ValidationError(result)
        return data


    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
        

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self,data):
        self.token = data['refresh']
        return data
    def save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except:
            raise ValidationError({'status':False,'message':'Could not find refresh token ad add to black list'})
        