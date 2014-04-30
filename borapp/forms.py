from django.forms import ModelForm

from borapp.models import *

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = [
            'name',
            'year',
            'grapes',
            'region',
            'winery',
            'comments',
        ]

class WineInRegionForm(ModelForm):
    class Meta:
        model = Wine
        exclude = ['region']

