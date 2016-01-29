from django.shortcuts import render
from django.http import HttpResponse
import json
from login.models import User
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def log(request):#,passw_hash):
    request_json = json.loads(request.body);
    username = request_json['username']
    passw = request_json['passw']
    try:
        user = User.objects.get(username__exact=str(username),passw__exact=str(passw))
    except:
        return JsonResponse({'success':False})
    request.session['username'] = username
    return JsonResponse({'success':True})
    # return HttpResponse('cuack')
def create(request):
    request_json = json.loads(request.body);
    username = request_json['username']
    passw = request_json['passw']
    try:
        user = User.objects.get(username__exact=str(username))
        return JsonResponse({'success':False})
    except :
        new_user = User(username=username, passw=passw)
        new_user.save()
        return JsonResponse({'success':True})

    return 0
