from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/patient', views.PatientAPIView, basename='patient')
router.register(r'api/procedure', views.ProcedureView, basename='procedure')
router.register(r'api/dental-chart', views.DentalChartView, basename='DentalChart')
urlpatterns = [

]
urlpatterns += router.urls
