from .views import MalariaViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'malaria', MalariaViewSet)
urlpatterns = router.urls