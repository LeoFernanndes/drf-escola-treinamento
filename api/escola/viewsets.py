from rest_framework import viewsets, status, response, exceptions
from escola.models import Escola, Curso
from escola.serializers import EscolaSerializer, CursoSerializer


class EscolaViewset(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

class CursoViwset(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_queryset(self):
        return self.queryset.filter(escola=self.kwargs.get('escolas_pk'))

    def validate_query_escola(self):
        if not Escola.objects.filter(id=self.kwargs.get('escolas_pk', 0)).exists():
            raise exceptions.NotFound()

    def create(self, request, *args, **kwargs):
        self.validate_query_escola()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, escolas_pk=kwargs.get('escolas_pk'))
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, **kwargs):
        data = serializer.validated_data
        data['escola'] = Escola.objects.get(id=kwargs['escolas_pk'])
        Curso.objects.create(**data)

    def list(self, request, *args, **kwargs):
        self.validate_query_escola()
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.validate_query_escola()
        return super().retrieve(request, *args, **kwargs)

