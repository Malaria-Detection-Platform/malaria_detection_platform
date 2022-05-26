from rest_framework import viewsets
from ..models import malaria
from .serializers import MalariaSerializer
class MalariaViewSet(viewsets.ModelViewSet):
    serializer_class = MalariaSerializer
    queryset = malaria.objects.all()
    