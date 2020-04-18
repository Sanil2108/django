from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from contactsApp.models import Car

def index(request):
    return Response({'data': 'Hello, world'},  status=status.HTTP_201_CREATED)

class ListCars(APIView):

    def get(self, request):
        # cars = Car.objects.all()
        return Response(
            {'data': 'Something'},
            # status = status.HTTP_201_CREATED
        )