from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from patient.models import Patient
from patient.serializer import PatientSerializer
from utils.utils import ErrorResponses


# Create your views here.
class PatientAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=True)
    def post(self, request: Request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        patient = Patient(first_name=data['first_name'],
                          last_name=data['last_name'],
                          gender=data['gender'],
                          birth_date=data['birth_date'],
                          email=data['email'],
                          phone=data['phone'],
                          address=data['address'],
                          allergies=data['allergies'],
                          job=data['job'],
                          emergency_name=data['emergency_name'],
                          emergency_contact=data['emergency_contact'])
        patient.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(methods='put', detail=True)
    def put(self, request: Request):
        id = request.data['id']
        try:
            patient = Patient.objects.get(pk=id)
            serializer = PatientSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            patient.first_name = data['first_name']
            patient.last_name = data['last_name']
            patient.gender = data['gender']
            patient.birth_date = data['birth_date']
            patient.email = data['email']
            patient.phone = data['phone']
            patient.address = data['address']
            patient.allergies = data['allergies']
            patient.job = data['job']
            patient.emergency_name = data['emergency_name']
            patient.emergency_contact = data['emergency_contact']
            patient.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Patient.DoesNotExist:
            return Response(detail=ErrorResponses.OBJECT_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
