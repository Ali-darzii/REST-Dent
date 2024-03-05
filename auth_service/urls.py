from django.urls import path
from . import views

urlpatterns = [
    path('api/user/auth/', views.AuthView.as_view(), name='auth'),
    path('api/user/logout/', views.UserLogout.as_view(), name='logout'),
]
