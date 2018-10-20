from django.shortcuts import render
from .forms import Register_form


def register(request):
    form = Register_form()
    return render(request, 'accounts/register.html', {'form': form})
