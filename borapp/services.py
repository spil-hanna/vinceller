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


def add_wine(form):
    form.save()
    # any post-procesing comes here


def update_wine(form):
    form.save()
    # any post-procesing comes here


def extra_check(form):
    # extra check: winery is from the correct region
    winery = form.cleaned_data.get('winery', None)
    region = form.cleaned_data.get('region', None)
    if winery and region and not is_in_region(winery, region):
        # TODO: raise validation error
        pass


