from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact

def index(request):
    return render(request, 'phonebook/index.html')

def create_new(request):
    return render(request, "phonebook/createnew.html")

def submit_new(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    contact = Contact(contact_name = name, phone = phone, email = email)
    contact.save()
    return render(request, "phonebook/submitnew.html")

def see_contacts(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request, "phonebook/seecontacts.html", context)