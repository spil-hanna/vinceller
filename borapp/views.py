from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from django.shortcuts import render
from django.http import HttpResponseRedirect

from borapp.models import *
from borapp.forms import *
from django import forms

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


class GrapeCreateView(CreateView):
    model = Grape
    template_name = 'borapp/edit_grape.html'
    
    def get_success_url(self):
        return reverse('grape-list')

    def get_context_data(self, **kwargs):

        context = super(GrapeCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('grape-new')

        return context


class GrapeUpdateView(UpdateView):
    model = Grape
    template_name = 'borapp/edit_grape.html'
    
    def get_success_url(self):
        return reverse('grape-list')

    def get_context_data(self, **kwargs):

        context = super(GrapeUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('grape-edit', kwargs={'pk': self.get_object().id})

        return context


class RegionListView(ListView):
    model = Region
    template_name = 'borapp/list_regions.html'


class RegionCreateView(CreateView):
    model = Region
    template_name = 'borapp/edit_region.html'
    
    def get_success_url(self):
        return reverse('region-list')

    def get_context_data(self, **kwargs):

        context = super(RegionCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('region-new')

        return context


class RegionUpdateView(UpdateView):
    model = Region
    template_name = 'borapp/edit_region.html'
    
    def get_success_url(self):
        return reverse('region-list')

    def get_context_data(self, **kwargs):

        context = super(RegionUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('region-edit', kwargs={'pk': self.get_object().id})

        return context


class YearListView(ListView):
    model = Year
    template_name = 'borapp/list_years.html'


class YearCreateView(CreateView):
    model = Year
    template_name = 'borapp/edit_year.html'
    
    def get_success_url(self):
        return reverse('year-list')

    def get_context_data(self, **kwargs):

        context = super(YearCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('year-new')

        return context


class YearUpdateView(UpdateView):
    model = Year
    template_name = 'borapp/edit_year.html'
    
    def get_success_url(self):
        return reverse('year-list')

    def get_context_data(self, **kwargs):

        context = super(YearUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('year-edit', kwargs={'pk': self.get_object().id})

        return context


class WineryListView(ListView):
    model = Winery
    template_name = 'borapp/list_wineries.html'


class WineryCreateView(CreateView):
    model = Winery
    template_name = 'borapp/edit_winery.html'
    
    def get_success_url(self):
        return reverse('winery-list')

    def get_context_data(self, **kwargs):

        context = super(WineryCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('winery-new')

        return context


class WineryUpdateView(UpdateView):
    model = Winery
    template_name = 'borapp/edit_winery.html'
    
    def get_success_url(self):
        return reverse('winery-list')

    def get_context_data(self, **kwargs):

        context = super(WineryUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('winery-edit', kwargs={'pk': self.get_object().id})

        return context


class WineListView(ListView):
    model = Wine
    template_name = 'borapp/list_wines.html'


class WineCreateView(CreateView):
    model = Wine
    template_name = 'borapp/edit_wine.html'
    
    def get_success_url(self):
        return reverse('wine-list')

    def get_context_data(self, **kwargs):

        context = super(WineCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('wine-new')

        return context


class WineUpdateView(UpdateView):
    model = Wine
    template_name = 'borapp/edit_wine.html'
    
    def get_success_url(self):
        return reverse('wine-list')

    def get_context_data(self, **kwargs):

        context = super(WineUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('wine-edit', kwargs={'pk': self.get_object().id})

        return context


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")


