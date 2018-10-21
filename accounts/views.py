from django.shortcuts import render, redirect
from .forms import Register_form, Login_form


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
    return render(request, 'accounts/login.html', {'form': Login_form()})

def profile(request):
    return render(request, 'accounts/profile.html', {})