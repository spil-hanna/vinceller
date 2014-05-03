from django.forms import ModelForm
from django.core.exceptions import ValidationError

from borapp.models import *
from borapp import services

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = [
            'name',
            'year',
            'grapes',
            'region',
            'winery',
        ]

    def clean(self):
        winery = self.cleaned_data.get('winery', None)
        region = self.cleaned_data.get('region', None)
        if winery and region and not services.is_in_region(winery, region):
            raise ValidationError("Winery is not in the correct region")
            pass


class WineInRegionForm(ModelForm):
    class Meta:
        model = Wine
        exclude = ['region']

