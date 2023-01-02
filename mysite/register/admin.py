from django.contrib import admin

from .models import Vendas, TipoVendas, PropesccaoValor


class VendasAdmin(admin.ModelAdmin):
    fields = ['nome_venda', 'tipo_venda', 'data_venda', 'data_aceite_cliente', 'valor_venda']
    search_fields = ['nome_venda', 'tipo_venda']


admin.site.register(Vendas, VendasAdmin)


class TipoVendasAdmin(admin.ModelAdmin):
    fields = ['tp_nome', 'tp_data_registro']
    search_fields = ['tp_nome']


admin.site.register(TipoVendas, TipoVendasAdmin)


class PropesccaoValorAdmin(admin.ModelAdmin):
    fields = ['ppv_vendas', 'ppv_valor', 'ppv_conversao', 'ppv_data']
    search_fields = ['ppv_vendas']


admin.site.register(PropesccaoValor, PropesccaoValorAdmin)