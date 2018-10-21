from django.http import Http404
from django.shortcuts import render
from .forms import Report_form, AdvertisementCreat_form
from .models import Advertisement


def index(request):
    return render(request, 'index.html')


def report(request, id):
    return render(request, 'report.html', {'form': Report_form()})


def advertisement(request, adv_id):
    try:
        adv = Advertisement.objects.get(pk=adv_id)
    except Advertisement.DoesNotExist:
        raise Http404("ogłoszenie nie istnieje ")
    return render(request, 'advertisement.html', {'advertisement': adv})


def advertisement_creat(request):
    return render(request, 'advertisement-create.html', {'form': AdvertisementCreat_form()})