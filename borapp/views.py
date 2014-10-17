from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django import forms
from django.forms.models import modelform_factory, inlineformset_factory
from django.http import HttpResponseRedirect

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.decorators import login_required

from borapp.models import *
from borapp.forms import *
from borapp import services

@login_required
def dashboard(request):
    wines = Wine.objects.all()
    return render(request, 'borapp/dashboard.html', {
        'wines': wines,
    })


'''
Grape views
The simplest set of CRUD forms
- generic views
- mofel forms (with form factory) 
'''
class GrapeListView(ListView):
    model = Grape
    template_name = 'borapp/list_grapes.html'

@login_required
def grapes_new(request):
    if request.method == 'POST':
        Form = modelform_factory(Grape, fields=('name',))
        form = Form(request.POST)
        try:
            form.save()
            return HttpResponseRedirect(reverse('grapes-list'))
        except ValueError:
            pass
    else:
        Form = modelform_factory(Grape, fields=('name',))
        form = Form()
    
    return render(request, 'borapp/edit_grape.html', {
        'form': form,
        'action': reverse('grapes-new'),
    })    


@login_required
def grapes_edit(request, pk):
    grape = get_object_or_404(Grape, pk=pk)
    
    if request.method == 'POST':
        Form = modelform_factory(Grape, fields=('name',))
        form = Form(request.POST, instance=grape)
        try:
            form.save()
            return HttpResponseRedirect(reverse('grapes-list'))
        except ValueError:
            pass
    else:
        Form = modelform_factory(Grape, fields=('name',))
        form = Form(instance=grape)
    
    return render(request, 'borapp/edit_grape.html', {
        'form': form,
        'action': reverse('grapes-edit', kwargs={'pk': grape.id}),
        'grape': grape,
    })    


'''
Views for Region and Winery
'''
class RegionListView(ListView):
    model = Region
    template_name = 'borapp/list_regions.html'


@login_required
def regions_new(request):
    if request.method == 'POST':
        Form = modelform_factory(Region, fields=('name',))
        form = Form(request.POST)
        WineryFormSet = inlineformset_factory(
            Region,
            Winery,
            fk_name='region',
            fields=('name', 'website',),
            can_delete=False,
            extra=1
        )
        formset = WineryFormSet(request.POST)
        try:
            region = form.save()
            formset.instance = region
            formset.save()
            return HttpResponseRedirect(reverse('regions-list'))
        except ValueError:
            pass
    else:
        Form = modelform_factory(Region, fields=('name',))
        form = Form()
        WineryFormSet = inlineformset_factory(
            Region,
            Winery,
            fk_name='region',
            fields=('name', 'website',),
            can_delete=False,
            extra=1
        )
        formset = WineryFormSet()
    
    return render(request, 'borapp/edit_region.html', {
        'region_form': form,
        'winery_forms': formset,
        'action': reverse('regions-new'),
    })    


@login_required
def regions_edit(request, pk):
    region = get_object_or_404(Region, pk=pk)
    
    if request.method == 'POST':
        Form = modelform_factory(Region, fields=('name',))
        form = Form(request.POST, instance=region)
        WineryFormSet = inlineformset_factory(
            Region,
            Winery,
            fk_name='region',
            fields=('name', 'website',),
            can_delete=False,
            extra=1
        )
        formset = WineryFormSet(request.POST, instance=region)
        try:
            form.save()
            formset.save()
            return HttpResponseRedirect(reverse('regions-list'))
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
        'action': reverse('regions-edit', kwargs={'pk': region.id}),
        'region': region,
    })    


class YearListView(ListView):
    model = Year
    template_name = 'borapp/list_years.html'


class WineryListView(ListView):
    model = Winery
    template_name = 'borapp/list_wineries.html'

'''
Views for wine, using
- handmade form
'''
class WineListView(ListView):
    model = Wine
    template_name = 'borapp/list_wines.html'


@login_required
def wines_new(request):
    if request.method == 'POST':
        form = WineForm(request.POST)
        try:
            services.add_wine(form)
            return HttpResponseRedirect(reverse('wines-list'))
        except ValueError:
            pass
    else:
        form = WineForm()
    
    return render(request, 'borapp/edit_wine.html', {
        'form': form,
        'action': reverse('wines-new'),
    })    


@login_required
def wines_edit(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
       
    if request.method == 'POST':
        form = WineForm(request.POST, instance=wine)
        try:
            services.update_wine(form)
            return HttpResponseRedirect(reverse('wines-list'))
        except ValueError:
            pass
    else:
        form = WineForm(instance=wine)
    
    return render(request, 'borapp/edit_wine.html', {
        'form': form,
        'action': reverse('wines-edit', kwargs={'pk': wine.id}),
        'wine': wine,
    })    


@login_required
def wineinregion(request, region_id):
    # region hardcoded
    region = get_object_or_404(Region, pk=region_id)
    if request.method == 'POST':
        form = WineInRegionForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('wines-list'))
    else:
        form = WineInRegionForm()
        form.fields['winery'] = forms.ModelChoiceField(Winery.objects.filter(region=region.pk))
        
    return render(request, 'borapp/wine_in_region.html', {
        'form': form,
        'region': region,
    })    


