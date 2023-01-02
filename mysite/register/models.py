import datetime
from time import timezone

from django.db import models


class Vendas(models.Model):
    vendas_id = models.BigAutoField(primary_key=True)
    nome_venda = models.CharField(max_length=200, null=False)
    tipo_venda = models.ForeignKey('TipoVendas', models.DO_NOTHING, db_column='tp_id', null=False)
    data_venda = models.DateTimeField(blank=True, null=False)
    data_aceite_cliente = models.DateTimeField(verbose_name='Data de aceite do cliente', blank=True, null=True)
    valor_venda = models.DecimalField(max_digits=19, decimal_places=2, null=False)

    def __str__(self):
        return f'{self.nome_venda}'

    # def was_registered_recently(self):
    # return self.data_venda >= timezone.now() - datetime.timedelta(days=1)


class TipoVendas(models.Model):
    tp_id = models.AutoField(primary_key=True)
    tp_nome = models.CharField(max_length=200, verbose_name='Nome')
    tp_data_registro = models.DateTimeField('data de registro', null=True)

    def __str__(self):
        return f'{self.tp_nome}'


class PropesccaoValor(models.Model):
    ppv_id = models.AutoField(primary_key=True)
    ppv_vendas = models.DecimalField(verbose_name='Prospecção de venda', null=False, max_digits=19, decimal_places=2)
    ppv_valor = models.DecimalField(max_digits=19, decimal_places=2, default='0')
    ppv_conversao = models.DecimalField(verbose_name='Conversão', null=False, max_digits=19, decimal_places=2)
    ppv_data = models.DateTimeField('Data para propescção', blank=True, null=False)

    def __str__(self):
        return f'{self.ppv_vendas}'



