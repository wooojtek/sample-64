__author__ = 'wb'
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # URL pattern for the ContactView
                       # url(regex=r'^contact/$', view=ContactFormView.as_view(), name='contact'),
                       url(regex=r'^faq/$', view='apps.faq.views.faq_index', name='faq_index'),
)