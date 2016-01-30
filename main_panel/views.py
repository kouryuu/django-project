from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from main_panel.models import Name
from django.http import JsonResponse

# Create your views here.
def main_index(request):
    names = Name.objects.get(id='1')
    username = request.session['username']
    context = {
    'username' : username,
    'name1' : names.name1,
    'name2' : names.name2,
    'name3' : names.name3
    }
    if username == None or username == '':
        return HttpResponseRedirect("/login/")
    else:
        return render(request, 'main_index.html',context)
def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect("/login/")
def changeName(request):
    request_json = json.loads(request.body)
    name1 = request_json['name1']
    name2 = request_json['name2']
    name3 = request_json['name3']
    names = Name.objects.get(id='1')
    names.name1 = name1
    names.name2 = name2
    names.name3 = name3
    try:
        names.save()
    except:
        return JsonResponse({'success':False})
    return JsonResponse({'success':True})
