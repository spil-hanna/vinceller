from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views

from borapp.views import *

urlpatterns = patterns('',

    url(r'^accounts/login/$', auth_views.login, {template_name: 'borapp/login.html'}),

    url(r'^$', dashboard,
        name='dashboard'),

    url(r'^grapes/$', GrapeListView.as_view(),
        name='grapes-list'),
    url(r'^grapes/new$',
        grapes_new,
        name='grapes-new',),
    url(r'^grapes/(?P<pk>\d+)/$',
        grapes_edit,
        name='grapes-edit'),

    url(r'^regions/$', RegionListView.as_view(),
        name='regions-list'),
    url(r'^regions/new$',
        regions_new,
        name='regions-new',),
    url(r'^regions/(?P<pk>\d+)/$',
        regions_edit,
        name='regions-edit'),

    url(r'^years/$', YearListView.as_view(),
        name='years-list'),

    url(r'^wineries/$', WineryListView.as_view(),
        name='wineries-list'),

    url(r'^wines/$', WineListView.as_view(),
        name='wines-list'),
    url(r'^wines/new$',
        wines_new,
        name='wines-new',),
    url(r'^wines/(?P<pk>\d+)/$',
        wines_edit,
        name='wines-edit'),

    url(r'^admin/', include(admin.site.urls)),

    # for testing
    url(r'^wineinregion/(?P<region_id>\d+)/$',
        wineinregion,
        name='wineinregion'),



)
