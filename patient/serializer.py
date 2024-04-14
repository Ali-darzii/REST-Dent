from django.core.validators import validate_email
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ValidationError
from utils.utils import ErrorResponses
from django.core.exceptions import ValidationError as NotValid
from patient.models import Patient, Procedure, DentalChart
from auth_service.models import UserLogins


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        exclude = ('user_logins',)

    def __init__(self, *args, **kwargs):
        super(PatientSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request.method == 'POST':
            self.fields['user_logins'] = PrimaryKeyRelatedField(queryset=UserLogins.objects.all())

    def validate_emergency_contact(self, value: str):
        if value.isdigit():
            if value.startswith('09'):
                return value
        raise ValidationError(detail=ErrorResponses.BAD_FORMAT)

    def validate_phone(self, value: str):
        if value.isdigit():
            if value.startswith('09'):
                return value
        raise ValidationError(detail=ErrorResponses.BAD_FORMAT)

    def validate_age(self, value: str):
        if not value.isdigit():
            ValidationError(detail=ErrorResponses.BAD_FORMAT)
        return value

    def validate_gender(self, value: str):
        if value not in ['male', 'female', 'other']:
            ValidationError(detail=ErrorResponses.BAD_FORMAT)
        return value

    def validate_email(self, value: str):
        try:
            validate_email(value)
            return value
        except NotValid:
            raise ValidationError(detail=ErrorResponses.BAD_FORMAT)


class ProcedureSerializer(ModelSerializer):
    class Meta:
        model = Procedure
        exclude = ('user_logins',)

    def __init__(self, *args, **kwargs):
        super(ProcedureSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request.method == 'POST':
            self.fields['user_logins'] = PrimaryKeyRelatedField(queryset=UserLogins.objects.all())


class DentalChartSerializer(ModelSerializer):
    class Meta:
        model = DentalChart
        fields = '__all__'

    def validate_adult_tooth(self, value: list):
        for item in value:
            if not isinstance(item, int) or not 18 <= item <= 48:
                raise ValidationError(detail=ErrorResponses.BAD_FORMAT)

        return value

    def validate_pediatric_tooth(self, value: list):
        for item in value:
            if not isinstance(item, int) or not 55 <= item <= 85:
                raise ValidationError(detail=ErrorResponses.BAD_FORMAT)

        return value

