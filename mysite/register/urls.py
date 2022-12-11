from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path(r'', views.index)
    # path('<int:vendas_id>/home', views.home, name='home')
]