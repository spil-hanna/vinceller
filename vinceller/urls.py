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
    url(r'^years/$', YearListView.as_view(),
        name='year-list'),
    url(r'^years/new$', YearCreateView.as_view(),
        name='year-new',),
    url(r'^wineries/$', WineryListView.as_view(),
        name='winery-list'),
    url(r'^wineries/new$', WineryCreateView.as_view(),
        name='winery-new',),
    url(r'^wines/$', WineListView.as_view(),
        name='wine-list'),
    url(r'^wines/new$', WineCreateView.as_view(),
        name='wine-new',),

    url(r'^admin/', include(admin.site.urls)),
)
