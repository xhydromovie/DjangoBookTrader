from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Register_form, Login_form
from django.contrib.auth import authenticate


def register(request):
    if request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = Register_form()
        return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                return HttpResponse('loged in, welcome')
            else:
                return render(request, 'accounts/login.html', {'form': Login_form()})

        else:
            return render(request, 'accounts/login.html', {'form': Login_form()})

    else:
        return render(request, 'accounts/login.html', {'form': Login_form()})


def profile(request):
    return render(request, 'accounts/profile.html', {})
