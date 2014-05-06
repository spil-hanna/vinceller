from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django import forms
from django.forms.models import modelform_factory, inlineformset_factory
from django.http import HttpResponseRedirect

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from borapp.models import *
from borapp.forms import *
from borapp import services


def dashboard(request):
    wines = Wine.objects.all()
    return render(request, 'borapp/dashboard.html', {
        'wines': wines,
    })


class GrapeListView(ListView):
    model = Grape
    template_name = 'borapp/list_grapes.html'


def grape_new(request):
    if request.method == 'POST':
        Form = modelform_factory(Grape, fields=('name',))
        form = Form(request.POST)
        try:
            form.save()
            return HttpResponseRedirect(reverse('grape-list'))
        except ValueError:
            pass
    else:
        Form = modelform_factory(Grape, fields=('name',))
        form = Form()
    
    return render(request, 'borapp/edit_grape.html', {
        'form': form,
        'action': reverse('grape-new'),
    })    


def grape_edit(request, pk):
    return HttpResponseRedirect(reverse('dashboard'))


class RegionListView(ListView):
    model = Region
    template_name = 'borapp/list_regions.html'


def region_new(request):
    if request.method == 'POST':
        Form = modelform_factory(Region, fields=('name',))
        form = Form(request.POST)
        try:
            form.save()
            return HttpResponseRedirect(reverse('region-list'))
        except ValueError:
            pass
    else:
        Form = modelform_factory(Region, fields=('name',))
        form = Form()
    
    return render(request, 'borapp/edit_region.html', {
        'region_form': form,
        'action': reverse('region-new'),
    })    


def region_edit(request, pk):
    region = get_object_or_404(Region, pk=pk)
    
    if request.method == 'POST':
        Form = modelform_factory(Region, fields=('name',))
        form = Form(request.POST, instance=region)
        WineryFormSet = inlineformset_factory(
            Region,
            Winery
        )
        formset = WineryFormSet(request.POST, instance=region)
        try:
            form.save()
            formset.save()
            return HttpResponseRedirect(reverse('region-list'))
        except ValueError:
            pass
    else:
        Form = modelform_factory(Region, fields=('name',))
        form = Form(instance=region)
        WineryFormSet = inlineformset_factory(
            Region,
            Winery,
            fk_name='region',
            fields=('name', 'website',),
            can_delete=False,
            extra=1
        )
        formset = WineryFormSet(instance=region)
    
    return render(request, 'borapp/edit_region.html', {
        'region_form': form,
        'winery_forms': formset,
        'action': reverse('region-edit', kwargs={'pk': region.id}),
        'region': region,
    })    


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
        form = WineForm(request.POST)
        try:
            services.add_wine(form)
            return HttpResponseRedirect(reverse('wine-list'))
        except ValueError:
            pass
    else:
        form = WineForm()
    
    return render(request, 'borapp/edit_wine.html', {
        'form': form,
        'action': reverse('wine-new'),
    })    


def wine_edit(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
       
    if request.method == 'POST':
        form = WineForm(request.POST, instance=wine)
        try:
            services.update_wine(form)
            return HttpResponseRedirect(reverse('wine-list'))
        except ValueError:
            pass
    else:
        form = WineForm(instance=wine)
    
    return render(request, 'borapp/edit_wine.html', {
        'form': form,
        'action': reverse('wine-edit', kwargs={'pk': wine.id}),
        'wine': wine,
    })    


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


