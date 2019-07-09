from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from signup.forms import SignUpForm

def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            
            name = form.cleaned_data['name']

            context = {'name':name, }

            return render(request, 'signup_done.html', context)

    
    form = SignUpForm(request.POST)
    return render(request, 'signup.html', {'form':form})