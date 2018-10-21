from django.shortcuts import render
from .forms import Report_form


def index(request):
    return render(request, 'index.html')

def report(request, id):
    return render(request, 'report.html', {'form': Report_form()})