from django.http import HttpRequest
from django.contrib.auth.models import User
from drf_yasg import openapi


def get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ErrorResponses:
    SOMETHING_WENT_WRONG = {'detail': "WE_ALSO_DON'T_KNOW_WHAT_HAPPENED!", 'error_code': 1}
    ALREADY_TAKEN = {'detail': 'ALREADY_TAKEN', 'error_code': 2}
    TOKEN_IS_EXPIRED_OR_INVALID = {'detail': 'TOKEN_IS_EXPIRED_OR_INVALID', 'error_code': 3}
    TARGET_USER_NOT_FOUND = {'detail': 'TARGET_USER_NOT_FOUND', 'error_code': 4}
    BAD_FORMAT = {'detail': 'BAD_FORMAT', 'error_code': 5}
    USER_NOT_FOUND = {'detail': 'USER_NOT_FOUND', 'error_code': 6}
    OBJECT_NOT_FOUND = {'detail': 'OBJECT_NOT_FOUND', 'error_code': 7}


# for document
class DocumentProperties:
    createPatientProperties = {
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'gender': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'birth_date': openapi.Schema(type=openapi.TYPE_STRING),
        'phone': openapi.Schema(type=openapi.TYPE_STRING),
        'address': openapi.Schema(type=openapi.TYPE_STRING),
        'job': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_name': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_contact': openapi.Schema(type=openapi.TYPE_STRING),
        'allergies': openapi.Schema(type=openapi.TYPE_STRING),
        'avatar': openapi.Schema(type=openapi.TYPE_STRING)

    }
    createPatientResponses = {
        'id': openapi.Schema(type=openapi.TYPE_STRING),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'gender': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'birth_date': openapi.Schema(type=openapi.TYPE_STRING),
        'phone': openapi.Schema(type=openapi.TYPE_STRING),
        'address': openapi.Schema(type=openapi.TYPE_STRING),
        'job': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_name': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_contact': openapi.Schema(type=openapi.TYPE_STRING),
        'allergies': openapi.Schema(type=openapi.TYPE_STRING),
        'avatar': openapi.Schema(type=openapi.TYPE_STRING),
        'time_stamp': openapi.Schema(type=openapi.TYPE_STRING)

    }

    updatePatientProperties = {
        'id': openapi.Schema(type=openapi.TYPE_STRING),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'gender': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'birth_date': openapi.Schema(type=openapi.TYPE_STRING),
        'phone': openapi.Schema(type=openapi.TYPE_STRING),
        'address': openapi.Schema(type=openapi.TYPE_STRING),
        'job': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_name': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_contact': openapi.Schema(type=openapi.TYPE_STRING),
        'allergies': openapi.Schema(type=openapi.TYPE_STRING),
        'avatar': openapi.Schema(type=openapi.TYPE_STRING),
    }
    updatePatientResponses = {
        'id': openapi.Schema(type=openapi.TYPE_STRING),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'gender': openapi.Schema(type=openapi.TYPE_STRING),
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'birth_date': openapi.Schema(type=openapi.TYPE_STRING),
        'phone': openapi.Schema(type=openapi.TYPE_STRING),
        'address': openapi.Schema(type=openapi.TYPE_STRING),
        'job': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_name': openapi.Schema(type=openapi.TYPE_STRING),
        'emergency_contact': openapi.Schema(type=openapi.TYPE_STRING),
        'allergies': openapi.Schema(type=openapi.TYPE_STRING),
        'avatar': openapi.Schema(type=openapi.TYPE_STRING),
        'time_stamp': openapi.Schema(type=openapi.TYPE_STRING)
    }

    authSignUpProperties = {
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING)
    }
    authResponses = {
        'access_token': openapi.Schema(type=openapi.TYPE_STRING),
        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING),
    }

    authLoginProperties = {
        'email': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    }
