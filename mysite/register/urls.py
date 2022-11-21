from django.urls import path, include
from django.contrib import admin
from . import views


admin.site.site_header = 'Registro de Vendas LABMAKER' #comando que renomeia o cabeçalho da App
admin.site.index_title = 'Bem-vindo ao LABMAKER' #comando que renomeia o título da página


urlpatterns = [
    path(r'', views.index)
    # path('<int:vendas_id>/home', views.home, name='home')
]