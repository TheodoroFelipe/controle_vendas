from django.contrib import admin

from .models import Vendas, TipoVendas


class VendasAdmin(admin.ModelAdmin):
    fields = ['tipo_venda', 'data_venda', 'data_aceite_cliente', 'valor_venda']
    search_fields = ['tipo_venda']


admin.site.register(Vendas, VendasAdmin)


class TipoVendasAdmin(admin.ModelAdmin):
    fields = ['nome', 'data_registro']
    search_fields = ['nome']


admin.site.register(TipoVendas, TipoVendasAdmin)
