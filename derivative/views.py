from django.shortcuts import render
from derivative.Derivative import *
import json
from django.http import JsonResponse

# Create your views here.
def getDerivative(request):
    request_json = json.loads(request.body)
    function = request_json['function']
    return JsonResponse({'derivative':derivative(function)})
