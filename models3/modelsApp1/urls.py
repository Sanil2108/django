from django.urls import path

from modelsApp1.views import hello_world

urlpatterns = [
    path('', hello_world),
]
