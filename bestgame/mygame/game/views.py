from django.http.response import  HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login
# Create your views here.
from models import PStartStatus

def signin(request):
    requestcontext = RequestContext(request)
    return render_to_response('sing.html', requestcontext)

def loginuser(request):
    requestcontext = RequestContext(request)
    user = authenticate(username = 'ivan',password = 'ivan')
    login(request, user)
    return render_to_response('choise.html', requestcontext)

def userchoise(request):
    requestcontext = RequestContext(request)
    all_charaters = PStartStatus.objects.all()
    requestcontext['choosable_charater'] = all_charaters
    return render_to_response('choise.html', requestcontext)
def choose(request, character_name):
    requestcontext = RequestContext(request)
    return render_to_response("game.html")