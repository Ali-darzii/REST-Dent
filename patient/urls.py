from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/patient', views.PatientAPIView, basename='patient')
urlpatterns = [

]
urlpatterns += router.urls
