from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_swagger_view(title='Malaria Detection App')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('malaria.urls', namespace='malaria')),
    path('api/', include('malaria_api.urls', namespace='malaria_api')),
    path('api/auth/', include('authentication.urls', namespace='authentication')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view),
    path('swagger/accounts', include('rest_framework.urls')),
    path('predict/', include('mlApi.api.urls')),
]
