from django import forms
from .models import Report

class Report_form(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('description',)