from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from patient.models import Patient, Procedure, DentalChart
from patient.serializer import PatientSerializer, ProcedureSerializer, DentalChartSerializer


# todo: avatar system in REST
class PatientAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_logins=self.request.user.user_logins)

    def create(self, request, *args, **kwargs):
        request.data['user_logins'] = self.request.user.user_logins.id
        return super().create(request, *args, **kwargs)


class ProcedureView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProcedureSerializer
    queryset = Procedure.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_logins=self.request.user.user_logins)

    def create(self, request, *args, **kwargs):
        request.data['user_logins'] = self.request.user.user_logins.id
        return super().create(request, *args, **kwargs)


class DentalChartView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DentalChartSerializer
    queryset = DentalChart.objects.all()

    def get_queryset(self):
        return self.queryset.filter(patient__user_logins=self.request.user.user_logins)


