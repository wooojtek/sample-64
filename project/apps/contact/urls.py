# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # URL pattern for the ContactView
                       # url(regex=r'^contact/$', view=ContactFormView.as_view(), name='contact'),
                       url(regex=r'^contact/$', view='apps.contact.views.contact', name='contact'),
)