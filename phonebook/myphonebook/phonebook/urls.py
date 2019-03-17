from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createnew/', views.create_new, name='Create new'),
    path('submitnew/', views.submit_new, name='Submit new'),
    path('seecontacts/', views.see_contacts, name='See contacts')
]
