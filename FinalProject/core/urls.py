from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Malaria Detection App')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('malaria.urls', namespace='malaria')),
    path('api/', include('malaria_api.urls', namespace='malaria_api')),
    path('api/auth/', include('authentication.urls', namespace='authentication')),
    path('swagger/', schema_view),
    path('swagger/accounts', include('rest_framework.urls')),
    path('predict/', include('mlApi.api.urls')),
]
