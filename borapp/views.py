from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

from borapp.models import *
from borapp.forms import *
from borapp import services

def wineinregion(request, region_id):
    # region hardcoded
    region = get_object_or_404(Region, pk=region_id)
    if request.method == 'POST':
        form = WineInRegionForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('wine-list'))
    else:
        form = WineInRegionForm()
        form.fields['winery'] = forms.ModelChoiceField(Winery.objects.filter(region=region.pk))
        
    return render(request, 'borapp/wine_in_region.html', {
        'form': form,
        'region': region,
    })    

class GrapeListView(ListView):
    model = Grape
    template_name = 'borapp/list_grapes.html'


class RegionListView(ListView):
    model = Region
    template_name = 'borapp/list_regions.html'


class YearListView(ListView):
    model = Year
    template_name = 'borapp/list_years.html'


class WineryListView(ListView):
    model = Winery
    template_name = 'borapp/list_wineries.html'


class WineListView(ListView):
    model = Wine
    template_name = 'borapp/list_wines.html'


def wine_new(request):
    if request.method == 'POST':
        services.add_wine(request.POST)
        return HttpResponseRedirect(reverse('wine-list'))
    else:
        form = WineForm()
    
    return render(request, 'borapp/edit_wine.html', {
        'form': form,
        'action': reverse('wine-new'),
    })    


def wine_edit(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
       
    if request.method == 'POST':
        services.update_wine(wine, request.POST)
        return HttpResponseRedirect(reverse('wine-list'))
    else:
        form = WineForm(instance=wine)
    
    return render(request, 'borapp/edit_wine.html', {
        'form': form,
        'action': reverse('wine-edit', kwargs={'pk': wine.id}),
        'wine': wine,
    })    



