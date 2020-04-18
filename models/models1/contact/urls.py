from django.urls import path

from contact.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name = 'Index view'),
]
