from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from signup.forms import SignUpForm, LoginForm

from signup.models import User

def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            cleaned_form = form.cleaned_data

            name = cleaned_form['name']
            email = cleaned_form['email']
            password = cleaned_form['password']

            user = User()
            user.email = email
            user.password = password
            user.name = name

            user.save()

            context = {'name':name, }

            return render(request, 'signup_done.html', context)

    
    form = SignUpForm(request.POST)
    return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cleaned_form = form.cleaned_data

            email = cleaned_form['email']
            password = cleaned_form['password']

            user = get_object_or_404(User, pk=email)
            if user.password == password:
                return render(request, 'login_done.html', {'email': email, 'success':True})
            else:
                return render(request, 'login_done.html', {'email': email, 'success':False})
    
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

