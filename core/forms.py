from django import forms

class QueryDistanceForm(forms.Form):
    source_address = forms.CharField(label='Source')
    destination_address = forms.CharField(label='Destination')