# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ContactFormView

urlpatterns = patterns('',
                       # URL pattern for the ContactView
                       url(regex=r'^contact/$', view=ContactFormView.as_view(), name='contact'),
)