from django.conf.urls import patterns, include, url
from django.contrib import admin

from borapp.views import *

urlpatterns = patterns('',
    url(r'^grapes/$', GrapeListView.as_view(),
        name='grape-list'),

    url(r'^regions/$', RegionListView.as_view(),
        name='region-list'),

    url(r'^years/$', YearListView.as_view(),
        name='year-list'),

    url(r'^wineries/$', WineryListView.as_view(),
        name='winery-list'),

    url(r'^wines/$', WineListView.as_view(),
        name='wine-list'),
    url(r'^wines/new$',
        wine_new,
        name='wine-new',),
    url(r'^wines/(?P<pk>\d+)/$',
        wine_edit,
        name='wine-edit'),

    url(r'^admin/', include(admin.site.urls)),

    # for testing
    url(r'^wineinregion/(?P<region_id>\d+)/$',
        wineinregion,
        name='wineinregion'),



)
