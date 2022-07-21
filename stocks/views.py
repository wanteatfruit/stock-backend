import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

# from mysite import stocks
from stocks.models import A
from stocks.models import B
from stocks.models import C

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the stocks index.")

def test(request):
    data = {}
    response = A.objects.all()
    data['list']=json.loads(serializers.serialize("json", response))
    print(data['list'])
    return HttpResponse(data['list'])