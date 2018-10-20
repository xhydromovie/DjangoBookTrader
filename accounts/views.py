from django.shortcuts import render
from .forms import Register_form, Login_form


def register(request):
    form = Register_form()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    return render(request, 'accounts/login.html', {'form': Login_form()})