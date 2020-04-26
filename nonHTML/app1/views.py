from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  # return HttpResponse('Hello world')
  image_data = open('/home/sanil/Desktop/181107171032-02-ww2-us-german-vets-painting-tank-super-tease.jpg', 'rb').read()

  response = HttpResponse(image_data, content_type="image/jpg")
  response['Content-Disposition'] = 'attachment; filename=tank.jpg'
  return response