# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ListQuestion, CreateQuestion, EditQuestion, DeleteQuestion


urlpatterns = patterns('',
                       url(r'^faq/$', ListQuestion.as_view(), name='list_question'),
                       url(r'^faq/create/$', CreateQuestion.as_view(), name='create_question'),
                       url(r'^faq/edit/(?P<pk>\d+)/$', EditQuestion.as_view(), name='edit_question'),
                       url(r'^faq/delete/(?P<pk>\d+)/$', DeleteQuestion.as_view(), name='delete_question'),
)