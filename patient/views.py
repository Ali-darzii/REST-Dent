from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from patient.models import Patient
from patient.serializer import PatientSerializer
from utils.utils import ErrorResponses, DocumentProperties
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# todo: avatar system in REST

# Create your views here.
class PatientAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        method='POST',
        operation_id='create_patient',
        operation_description='creating new patient (IsAuthenticated)',
        responses={
            201: openapi.Response(
                description='returning created data',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT, properties=DocumentProperties.createPatientResponses),
            )},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['first_name', 'last_name', 'gender'],
            properties=DocumentProperties.createPatientProperties
        )
    )
    @action(methods=['post'], detail=True)
    def post(self, request: Request):
        """ Create a new patient """
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        patient = Patient(first_name=data['first_name'],
                          last_name=data['last_name'],
                          gender=data['gender'],
                          birth_date=data.get('birth_date'),
                          email=data.get('email'),
                          phone=data.get('phone'),
                          address=data.get('address'),
                          allergies=data.get('allergies'),
                          job=data.get('job'),
                          emergency_name=data.get('emergency_name'),
                          emergency_contact=data.get('emergency_contact'),
                          user=request.user.user_logins
                          )
        patient.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        method='PUT',
        operation_id='update_patient',
        operation_description='update patient (IsAuthenticated)',
        responses={
            201: openapi.Response(
                description='returning updated data',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties=DocumentProperties.updatePatientResponses),

            )},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id', 'first_name', 'last_name', 'gender'],
            properties=DocumentProperties.updatePatientProperties
        )
    )
    @action(methods=['put'], detail=True)
    def put(self, request: Request):
        """ Update an existing patient """
        id = request.data['id']
        try:
            serializer = PatientSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            print(data)
            patient = Patient.objects.get(pk=id)
            patient.first_name = data['first_name']
            patient.last_name = data['last_name']
            patient.gender = data['gender']
            patient.birth_date = data.get('birth_date')
            patient.email = data.get('email')
            patient.phone = data.get('phone')
            patient.address = data.get('address')
            patient.allergies = data.get('allergies')
            patient.job = data.get('job')
            patient.emergency_name = data.get('emergency_name')
            patient.emergency_contact = data.get('emergency_contact')
            patient.save()
            # add id (don't know why id is in it !)
            data['id'] = id
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Patient.DoesNotExist:
            return Response(detail=ErrorResponses.OBJECT_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)


class PatientReadOnlyView(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    model = Patient
    queryset = Patient.objects.all()
