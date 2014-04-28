from django.conf.urls import patterns, include, url
from django.contrib import admin

from borapp.views import *

urlpatterns = patterns('',
    url(r'^grapes/$', GrapeListView.as_view(),
        name='grape-list'),
    url(r'^grapes/new$', GrapeCreateView.as_view(),
        name='grape-new',),
    url(r'^grapes/(?P<pk>\d+)/$',
        GrapeUpdateView.as_view(),
        name='grape-edit'),

    url(r'^regions/$', RegionListView.as_view(),
        name='region-list'),
    url(r'^regions/new$', RegionCreateView.as_view(),
        name='region-new',),
    url(r'^regions/(?P<pk>\d+)/$',
        RegionUpdateView.as_view(),
        name='region-edit'),

    url(r'^years/$', YearListView.as_view(),
        name='year-list'),
    url(r'^years/new$', YearCreateView.as_view(),
        name='year-new',),
    url(r'^years/(?P<pk>\d+)/$',
        YearUpdateView.as_view(),
        name='year-edit'),

    url(r'^wineries/$', WineryListView.as_view(),
        name='winery-list'),
    url(r'^wineries/new$', WineryCreateView.as_view(),
        name='winery-new',),
    url(r'^wineries/(?P<pk>\d+)/$',
        WineryUpdateView.as_view(),
        name='winery-edit'),

    url(r'^wines/$', WineListView.as_view(),
        name='wine-list'),
    url(r'^wines/new$', WineCreateView.as_view(),
        name='wine-new',),
    url(r'^wines/(?P<pk>\d+)/$',
        WineUpdateView.as_view(),
        name='wine-edit'),

    url(r'^admin/', include(admin.site.urls)),

    # for testing
    url(r'^wineinregion/(?P<region_id>\d+)/$',
        wineinregion,
        name='wineinregion'),



)
