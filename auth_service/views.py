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
from utils.utils import ErrorResponses


class AuthView(APIView):
    allowed_methods = ['post', 'put']

    @action(methods=['post'], detail=True)
    def post(self, request):
        """ signup """
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

    # todo: how check with jwt that not authenticated !
    @action(methods=['put'], detail=True)
    def put(self, request: Request):
        """ login """
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


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    # without serializer
    @action(['post'], detail=True)
    def post(self, request: Request):
        """ logout user """
        try:
            refresh_token = request.data['tk']
            tk = RefreshToken(refresh_token)
            tk.blacklist()
            return Response(data='Successfully logged out.', status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(data=ErrorResponses.TOKEN_IS_EXPIRED_OR_INVALID, status=status.HTTP_400_BAD_REQUEST)
