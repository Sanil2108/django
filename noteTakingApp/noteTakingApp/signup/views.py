from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def signup_done(request):
    return HttpResponse(request)