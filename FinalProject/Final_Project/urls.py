from django.contrib import admin
from django.urls import path, include
from Final_Project import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
# from django.views.generic import RedirectView
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
    path('hospital/', views.hospital_list),
    path('person/', views.person_list),
    path('credential/', views.credential_list),
    path('request_diagnostic/', views.request_diagnostic_list),
    path('patient/', views.patient_list),
    path('prescription/', views.prescription_list),
    path('hospital/<int:id>', views.hospital_detail),
    path('person/<int:id>', views.person_detail),
    path('credential/<int:id>', views.credential_detail),
    path('request_diagnostic/<int:id>', views.request_diagnostic_detail),
    path('patient/<int:id>', views.patient_detail),
    path('prescription/<int:id>', views.prescription_detail),
    path('predict/', include('mlApi.api.urls')),
    

    path('swagger.json', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', 
        cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', 
        cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
