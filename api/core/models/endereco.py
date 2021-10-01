from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField(null=True)
    complemento = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.logradouro} {self.endereco}, {self.numero} {self.complemento}"

    class Meta:
        db_table = 'endereco'
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"
