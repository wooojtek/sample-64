# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^faq/$', 'apps.faq.views.faq_index', name='faq_index'),
                       url(r'^faq/question(?P<slug>[\w\-]+)/$', 'apps.faq.views.question', name='question'),
                       url(r'^faq/question_type/(?P<slug>[\w\-]+)/$', 'apps.faq.views.question_type',
                           name='question_type'),
)