from django.shortcuts import render
from django.http import JsonResponse
import stocks

# Create your views here.
def query(request, table_name):
    model = getattr(stocks.models, table_name)
    response = model.objects.all()
    data = list(response.values())
    return JsonResponse(data, safe=False)