from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Vendas


#def index(request):
 #   latest_vendas_list = Vendas.ordering('data_aceite_cliente')[:5]
  #  context = {'latest_vendas_list': latest_vendas_list}
   # return render(request, 'register/index.html', context)

def index(request):
    return render(request, r'C:\Users\T002565\PycharmProjects\ValorMaker\mysite\register\templates\register\index.html')

def home(request, vendas_id):
    return HttpResponse('Lista aqui' % vendas_id)
