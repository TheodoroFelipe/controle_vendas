import datetime
from time import timezone

from django.db import models


class Vendas(models.Model):
    vendas_id = models.BigAutoField(primary_key=True)
    tipo_venda = models.ForeignKey('TipoVendas', models.DO_NOTHING, db_column='tp_id', null=False)
    data_venda = models.DateTimeField(blank=True, null=False)
    data_aceite_cliente = models.DateTimeField('data', blank=True, null=True)
    valor_venda = models.DecimalField(max_digits=19, decimal_places=2, null=False)

    def __str__(self):
        return f'{self.tipo_venda}'

    def was_registered_recently(self):
        return self.data_venda >= timezone.now() - datetime.timedelta(days=1)


class TipoVendas(models.Model):
    tp_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    data_registro = models.DateTimeField('data de registro')

    def __str__(self):
        return self.nome
