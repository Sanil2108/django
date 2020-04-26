from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
  return render(request, 'helloworld.html', {'someVariable': 'Hello world'})
  # return HttpResponse('Hello world')
