from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def main_index(request):
    username = request.session['username']

    context = {
    'username' : username,
    'name1' : 'Edit Names',
    'name2' : 'Derivative',
    'name3' : 'Item Selection'
    }
    if username == None or username == '':
        return HttpResponseRedirect("/login/")
    else:
        return render(request, 'main_index.html',context)
def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect("/login/")
