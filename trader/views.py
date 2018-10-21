from django.shortcuts import render
from .forms import Report_form, AdvertisementCreat_form


def index(request):
    return render(request, 'index.html')

def report(request, id):
    return render(request, 'report.html', {'form': Report_form()})

def advertisement_creat(request):
    return render(request, 'advertisement-create.html', {'form': AdvertisementCreat_form()})