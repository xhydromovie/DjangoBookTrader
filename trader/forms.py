from django import forms
from .models import Report, Advertisement

class Report_form(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('description',)

class AdvertisementCreat_form(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'description')