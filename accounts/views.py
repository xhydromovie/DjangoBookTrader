from django.shortcuts import render
from .forms import Register_form, Login_form
from django.http import Http404
from django.contrib.auth.models import User


def register(request):
    form = Register_form()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    return render(request, 'accounts/login.html', {'form': Login_form()})

def myprofile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def profile(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        raise Http404('Nie ma takiego usera')
    return render(request, 'accounts/profile.html', {'user': user})