from django.forms import ModelForm

from borapp.models import *

class WineInRegionForm(ModelForm):
    class Meta:
        model = Wine
        exclude = ['region']


