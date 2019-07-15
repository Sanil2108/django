from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import forms

def form1(request):
    if request.method == 'POST':
        form = forms.NameForm()
        if form.is_valid():
            return HttpResponse('Hello')
        return HttpResponse('Hello2')
    else:
        form = forms.NameForm()
        return render(request, 'name.html', {'form':form})
