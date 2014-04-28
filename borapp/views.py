from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from borapp.models import *

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

class GrapeListView(ListView):
    model = Grape
    template_name = 'borapp/list_grapes.html'

class RegionCreateView(CreateView):
    model = Region
    template_name = 'borapp/edit_region.html'
    
    def get_success_url(self):
        return reverse('region-list')

class RegionListView(ListView):
    model = Region
    template_name = 'borapp/base.html'

class YearCreateView(CreateView):
    model = Year
    template_name = 'borapp/edit_year.html'
    
    def get_success_url(self):
        return reverse('year-list')

class YearListView(ListView):
    model = Year
    template_name = 'borapp/base.html'

class WineryCreateView(CreateView):
    model = Winery
    template_name = 'borapp/edit_winery.html'
    
    def get_success_url(self):
        return reverse('winery-list')

class WineryListView(ListView):
    model = Winery
    template_name = 'borapp/base.html'

class WineCreateView(CreateView):
    model = Wine
    template_name = 'borapp/edit_wine.html'
    
    def get_success_url(self):
        return reverse('wine-list')

class WineListView(ListView):
    model = Wine
    template_name = 'borapp/base.html'

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")


