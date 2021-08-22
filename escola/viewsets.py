from rest_framework import viewsets
from escola.models import Escola
from escola.serializers import EscolaSerializer


class EscolaViewset(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
