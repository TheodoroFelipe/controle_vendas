from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Registro de Vendas LABMAKER'  # comando que renomeia o cabeçalho da App
admin.site.index_title = 'Bem-vindo ao LABMAKER'  # comando que renomeia o título da página
admin.site.site_title = 'Registro de Vendas LabMaker'


urlpatterns = [

    path(r'admin/', admin.site.urls),
    path(r'', include('register.urls')),
    path('auth/', include('usuarios.urls'))
]
