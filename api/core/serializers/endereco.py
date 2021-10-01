from rest_framework import serializers
from core.models.endereco import Endereco


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = "__all__"
