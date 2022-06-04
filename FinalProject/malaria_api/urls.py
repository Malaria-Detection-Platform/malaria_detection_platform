from django.contrib import admin
from django.urls import path, include
from malaria_api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
# from django.views.generic import RedirectView

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
    # path('' , RedirectView.as_view(url ="/hospital/")),
    path('hospital/', views.HospitalList.as_view(), name='create_hospital_list'),
    path('registered_personnel/', views.RegisteredPersonnelList.as_view(),
         name='create_registered_personnel_list'),
    path('credential/', views.CredentialList.as_view(),
         name='create_credential_list'),
    path('request_diagnostic/', views.RequestDiagnosticList.as_view(),
         name='create_request_diagnostic_list'),
    path('patient/', views.PatientList.as_view(), name='create_patient_list'),
    path('patient_checkup/', views.PatientCheckupList.as_view(),
         name='create_patient_checkup_list'),
    path('prescription/', views.PrescriptionList.as_view(),
         name='create_prescription_list'),
    path('hospital/<int:id>', views.HospitalDetail.as_view(),
         name='create_hospital_detail_list'),
    path('registered_personnel/<int:id>', views.RegisteredPersonnelDetail.as_view(),
         name='registered_personnel_detail_list'),
    path('credential/<int:id>', views.CredentialDetail.as_view(),
         name='create_credential_detail_list'),
    path('request_diagnostic/<int:id>',
         views.RequestDiagnosticDetail.as_view(), name='create_hospital_list'),
    path('patient/<int:id>', views.PatientDetail.as_view(),
         name='create_patient_detail_list'),
    path('patient_checkup/<int:id>', views.PatientCheckupDetail.as_view(),
         name='create_patient_checkup_detail_list'),
    path('prescription/<int:id>', views.PrescriptionDetail.as_view(),
         name='create_prescription_detail_list'),
    path('predict/', include('mlApi.api.urls')),


    path('swagger.json', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
