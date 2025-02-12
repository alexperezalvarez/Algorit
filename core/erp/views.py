from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.erp.models import Product, Category

def myfierstview(request):
  data = {
    'name': 'Breynner',
    'categories': Category.objects.all()
    
  }
  return render(request, 'index.html', data)

def mysecondview(request):
  data = {
    'name': 'Breynner',
    'products': Product.objects.all()
    
  }
  return render(request, 'second.html', data)