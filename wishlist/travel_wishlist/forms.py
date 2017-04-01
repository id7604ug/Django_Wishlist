from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

class ShowPlaceInfoForm(forms.ModelForm):
    class Meta:
        model = Place
        fields  = ('name', 'visited', 'date_visited', 'review')
    # name = forms.CharField()
    # visited = forms.BooleanField()
    # date_visited = forms.DateField()
    # review = forms.CharField()
