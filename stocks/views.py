
import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from mysite import stocks
from stocks.models import A
from stocks.models import B
from stocks.models import C

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the stocks index.")

def test(request):
    response = A.objects.all()
    data = list(response.values())
    return JsonResponse(data, safe=False)
    # response_json=serializers.serialize('json',response)
    # return HttpResponse(response_json)
    # data['list']=json.loads(serializers.serialize("json", response))
    # print(type(data['list']))
    # return HttpResponse(data['list'])