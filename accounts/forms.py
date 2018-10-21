from django import forms
from django.contrib.auth.models import User


class Register_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class Login_form(forms.Form):
    username = forms.CharField(label='username', max_length=120)
    password = forms.CharField(label='password', max_length=120, widget=forms.PasswordInput())
