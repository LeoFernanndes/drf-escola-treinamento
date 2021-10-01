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

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    nivel = models.CharField(max_length=255)
    preco = models.FloatField()
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)
