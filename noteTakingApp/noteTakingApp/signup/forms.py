from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    password.widget.attrs.update({'type':'password'})

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

    password.widget.attrs.update({'type':'password'})