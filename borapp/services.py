from borapp.models import *
from borapp.forms import *


def get_allowed_wineries(region):
    w1 = Winery.objects.filter(region=region)
    w2 = Winery.objects.filter(region__isnull=True)
    return w1 | w2


def is_in_region(winery, region):
    if not winery.region:
        return True
    return winery.region == region


def add_wine(data):
    # parse, validate, save, post-process
    form = WineForm(data)
    if form.is_valid():
        # extra check: winery is from the correct region
        winery = form.cleaned_data['winery']
        region = form.cleaned_data['region']
        if is_in_region(winery, region):
            form.save()
        else:
            # TODO: raise validation error
            pass
        # post processing

def update_wine(wine, data):
    # parse, validate, save, post-process
    form = WineForm(data, instance=wine)
    if form.is_valid():
        # extra check: winery is from the correct region
        winery = form.cleaned_data['winery']
        region = form.cleaned_data['region']
        if is_in_region(winery, region):
            form.save()
        else:
            # TODO: raise validation error
            pass
        # post processing


