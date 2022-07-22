
import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from mysite import stocks
from stocks.models import A
from stocks.models import B
from stocks.models import C
import stocks

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the stocks index.")

# def test(request):
#     response = A.objects.all()
#     data = list(response.values())
#     return JssonResponse(data, safe=False)
    

def query(request, table_name):
    model = getattr(stocks.models, table_name)
    response = model.objects.all()
    data = list(response.values())
    return JsonResponse(data, safe=False)

# def query(request, table_name):
#     return HttpResponse("Hello world")