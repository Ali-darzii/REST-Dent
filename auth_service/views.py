from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import SignupSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth import user_logged_in
from rest_framework.decorators import action
from utils.utils import ErrorResponses, DocumentProperties
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class AuthView(APIView):
    # line allowed_methods not working with request body of swagger
    # allowed_methods = ['post', 'put', 'get']

    @swagger_auto_schema(
        method='POST',
        operation_id='user_signup',
        operation_description='creating user (not logged in indeed)',
        responses={201: openapi.Response(description='returning JWT',
                                         schema=openapi.Schema(
                                             type=openapi.TYPE_OBJECT, properties=DocumentProperties.authResponses),

                                         )},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'first_name', 'last_name', 'password'],
            properties=DocumentProperties.authSignUpProperties
        )
    )
    @action(methods=['post'], detail=True)
    def post(self, request: Request):
        """ signup """
        if not request.user.is_authenticated:
            serializer = SignupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user: User = User(email=serializer.validated_data['email'],
                              first_name=serializer.validated_data['first_name'],
                              last_name=serializer.validated_data['last_name'],
                              username=serializer.validated_data['email'],
                              is_active=True)
            user.set_password(serializer.validated_data['password'])
            user.last_login = timezone.now()
            user.save()
            user_logged_in.send(sender=self.__class__, request=request, user=user)
            data = {
                "access_token": str(AccessToken.for_user(user)),
                "refresh_token": str(RefreshToken.for_user(user)),
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=ErrorResponses.BAD_FORMAT, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        method='PUT',
        operation_id='user_login',
        operation_description='login user (not logged in indeed)',
        responses={200: openapi.Response(description='returning JWT',
                                         schema=openapi.Schema(
                                             type=openapi.TYPE_OBJECT, properties=DocumentProperties.authResponses),
                                         )},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties=DocumentProperties.authSignUpProperties
        )
    )
    @action(methods=['put'], detail=True)
    def put(self, request: Request):
        """ login """
        if not request.user.is_authenticated:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            try:
                user: User = User.objects.get(email=serializer.validated_data['email'], is_active=True)
                if user.check_password(serializer.validated_data['password']):
                    user.last_login = timezone.now()
                    user.save()
                    data = {
                        "access_token": str(AccessToken.for_user(user)),
                        "refresh_token": str(RefreshToken.for_user(user))
                    }
                    return Response(data=data, status=status.HTTP_200_OK)
                else:
                    return Response(data=ErrorResponses.TOKEN_IS_EXPIRED_OR_INVALID, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response(data=ErrorResponses.USER_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        return Response(data=ErrorResponses.BAD_FORMAT, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    # without serializer

    @swagger_auto_schema(
        method='POST',
        operation_id='user_logout',
        operation_description='user logout (Authenticated in indeed)',
        responses={204: openapi.Response(description='returning success')},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['refresh_token'],
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING),
            }
        )
    )
    @action(['post'], detail=True)
    def post(self, request: Request):
        """ logout user """
        try:
            refresh_token = request.data['refresh_token']
            tk = RefreshToken(refresh_token)
            tk.blacklist()
            return Response(data='Successfully logged out.', status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(data=ErrorResponses.TOKEN_IS_EXPIRED_OR_INVALID, status=status.HTTP_400_BAD_REQUEST)
