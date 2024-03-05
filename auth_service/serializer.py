from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from utils.utils import ErrorResponses


class SignupSerializer(serializers.ModelSerializer):
    # default: allow_blank = False
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    email = serializers.CharField(required=True, max_length=150)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

    def validate_email(self, value):
        """ Validate email and username exist check """
        try:
            validate_email(value)
            if not User.objects.filter(email=value).exists():
                return value
            else:
                raise serializers.ValidationError(detail=ErrorResponses.ALREADY_TAKEN)

        except ValidationError:
            raise serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)

    def validate_password(self, value: str):
        """
         3 parameters:
         1- 8 character >=
         2- numeric and character
         3- use 1 sign character
         """
        symbols = r'[!@#$%^&*()\[\]{}|\\/:;"\'<>,.?]'
        if len(value) >= 8:
            if re.search('[1-9]', value) and re.search('[a-z]', value):
                if re.search(symbols, value):
                    return value
                else:
                    raise serializers.ValidationError(detail='must contain at least 1 symbol ')
            else:
                raise serializers.ValidationError(detail='must contain numeric and character')
        else:
            raise serializers.ValidationError(detail='must contain 8 character or more')


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_email(self, value):
        """ Validate email  """
        try:
            validate_email(value)
            return value
        except ValidationError:
            raise serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)
