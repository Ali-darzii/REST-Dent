from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from patient.models import Patient
from patient.serializer import PatientSerializer


# todo: avatar system in REST

class PatientAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_logins=self.request.user.user_logins)

    def create(self, request, *args, **kwargs):
        request.data['user_logins'] = self.request.user.user_logins.id
        return super().create(request, *args, **kwargs)
