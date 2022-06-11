from rest_framework import serializers
from .models import User
from malaria import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'user_name', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}


class RegisteredPersonnelSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['user_name', 'email', 'role',
                  'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            user_name=self.validated_data['user_name'],
            email=self.validated_data['email']

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "Password mismatch"})
        user.set_password(password)
        user.role = self.validated_data['role']
        user.save()
        models.RegisteredPersonnel.objects.create(user=user)
        return user


class HospitalSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            user_name=self.validated_data['user_name'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "Password mismatch"})
        user.set_password(password)
        user.role = "hospital"
        user.save()
        models.Hospital.objects.create(user=user)
        return user


class AdminSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            user_name=self.validated_data['user_name'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "Password mismatch"})
        user.set_password(password)
        user.role = "admin"
        user.save()
        models.RegisteredPersonnel.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
