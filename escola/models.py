from django.db import models
from core.models.endereco import Endereco


class Escola(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.PROTECT,
        related_name='escola',
        verbose_name='Endereco',
        null=False
    )