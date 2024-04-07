from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.fields import CharField

from utils.utils import ErrorResponses
from django.core.exceptions import ValidationError
from patient.models import Patient
from auth_service.models import UserLogins


class PatientSerializer(serializers.ModelSerializer):
    # user_logins = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Patient
        exclude = ['user_logins']

    def __init__(self, *args, **kwargs):
        super(PatientSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request.method == 'POST':
            self.fields['user_logins'] = serializers.PrimaryKeyRelatedField(queryset=UserLogins.objects.all())

    def validate_emergency_contact(self, value: str):
        if value.isdigit():
            if value.startswith('09'):
                return value
        raise serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)

    def validate_phone(self, value: str):
        if value.isdigit():
            if value.startswith('09'):
                return value
        raise serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)

    def validate_age(self, value: str):
        if not value.isdigit():
            serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)
        return value

    def validate_gender(self, value: str):
        if value not in ['male', 'female', 'other']:
            serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)
        return value

    def validate_email(self, value: str):
        try:
            validate_email(value)
            return value
        except ValidationError:
            raise serializers.ValidationError(detail=ErrorResponses.BAD_FORMAT)
