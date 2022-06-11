from django.urls import path
from .views import PersonnelSignupView, HospitalSignupView, AdminSignupView, UserLoginView

app_name = 'authentication'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register_personnel/', PersonnelSignupView.as_view(),
         name='register_personnel'),
    path('register_hospital/', HospitalSignupView.as_view(),
         name='register_hospital'),
    path('register_admin/', AdminSignupView.as_view(),
         name='register_admin'),
]
