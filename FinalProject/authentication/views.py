from rest_framework import generics, permissions, status
from rest_framework.response import Response
from . import serializers
import coreapi
from .custom_permissions import isAdmin
from rest_framework.schemas import AutoSchema


class AuthViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('desc')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class PersonnelSignupView(generics.GenericAPIView):
    schema = AuthViewSchema()

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegisteredPersonnelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })


class HospitalSignupView(generics.GenericAPIView):
    schema = AuthViewSchema()

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.HospitalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })


class AdminSignupView(generics.GenericAPIView):
    schema = AuthViewSchema()

    permission_classes = [permissions.IsAuthenticated & isAdmin]
    serializer_class = serializers.AdminSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })


class UserLoginView(generics.GenericAPIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)
