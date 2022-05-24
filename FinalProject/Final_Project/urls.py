from django.contrib import admin
from django.urls import path
from Final_Project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', views.hospital_list),
    path('person/', views.person_list),
    path('cedential/', views.credential_list),
    path('request_diagnostic/', views.request_diagnostic_list),
    path('patient/', views.patient_list),
    path('prescription/', views.prescription_list),
    path('hospital/<int:id>', views.hospital_detail),
    path('person/<int:id>', views.person_detail),
    path('cedential/<int:id>', views.credential_detail),
    path('request_diagnostic/<int:id>', views.request_diagnostic_detail),
    path('patient/<int:id>', views.patient_detail),
    path('prescription/<int:id>', views.prescription_detail),
]
