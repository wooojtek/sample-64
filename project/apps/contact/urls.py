# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import CreateContact


urlpatterns = patterns('',
                       # URL pattern for the ContactView
                       url(r'^contact/$', CreateContact.as_view(), name='contact'),
)