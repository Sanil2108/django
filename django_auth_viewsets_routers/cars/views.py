from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework import viewsets
from rest_framework.decorators import action

from cars.models import Car, Engine

from cars.serializers import CarSerializer, EngineSerializer

class MyAnonRateThrottle(AnonRateThrottle):
    def __init__(self):
        self.rate = 10
        self.num_requests = 10
        self.duration = 100

# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):
        return Response('Hello world' + str(request.user))

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    throttle_classes = [MyAnonRateThrottle]

    @action(detail = False)
    def do_something(self, request):
        print('Running do_something in CarViewSet')
        print(request)

        return Response('Done something')

class EngineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer