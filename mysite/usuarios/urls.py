from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name="cadastrar_vendedor"),
    path('login/', views.login, name="login"),
    path('sair/', views.logout, name="sair")
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
