from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/read-only/patient', views.PatientReadOnlyView, basename='patientReadOnly')
urlpatterns = [
    path('api/patient/', views.PatientAPIView.as_view()),

]
urlpatterns += router.urls
