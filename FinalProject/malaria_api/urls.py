from django.contrib import admin
from django.urls import path, include
from malaria_api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

app_name = 'malaria_api'

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes={}
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', views.HospitalList.as_view(), name='create_hospital_list'),
    path('registered_personnel/', views.RegisteredPersonnelList.as_view(),
         name='create_registered_personnel_list'),
    path('request_diagnostic/', views.RequestDiagnosticList.as_view(),
         name='create_request_diagnostic_list'),
    path('patient/', views.ReceptionistPatientList.as_view(),
         name='create_patient_list'),
    path('patient_checkup/', views.PatientCheckupList.as_view(),
         name='create_patient_checkup_list'),
    path('prescription/', views.PrescriptionList.as_view(),
         name='create_prescription_list'),
    path('hospital/<int:pk>', views.HospitalDetail.as_view(),
         name='create_hospital_detail_list'),
    path('registered_personnel/<int:pk>', views.RegisteredPersonnelDetail.as_view(),
         name='registered_personnel_detail_list'),
    path('request_diagnostic/<int:pk>',
         views.RequestDiagnosticDetail.as_view(), name='create_hospital_list'),
    path('patient/<int:pk>', views.ReceptionistPatientDetail.as_view(),
         name='create_patient_detail_list'),
    path('patient_checkup/<int:pk>', views.PatientCheckupList.as_view(),
         name='create_patient_checkup_detail_list'),
    path('prescription/<int:pk>', views.PrescriptionDetail.as_view(),
         name='create_prescription_detail_list'),
    path('receptionist_patient_list/', views.ReceptionistPatientList.as_view(),
         name='create_prescription_detail_list'),
    path('receptionist_patient_detail/<int:pk>', views.ReceptionistPatientDetail.as_view(),
         name='create_prescription_detail_list'),
    path('doctor_patient_list/', views.DoctorPatientList.as_view(),
         name='create_prescription_detail_list'),
    path('doctor_patient_detail/<int:pk>', views.DoctorPatientDetail.as_view(),
         name='create_prescription_detail_list'),
]
