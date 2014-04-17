# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ListPost, DetailPost


urlpatterns = patterns('',
                       url(r'^blog/$', ListPost.as_view(), name='list_post'),
                       url(r'^blog/(?P<slug>[\w\-]+)/$', DetailPost.as_view(), name='detail_post'),
)