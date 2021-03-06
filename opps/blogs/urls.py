#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.decorators.cache import cache_page

from .views import PostBlogList, PostBlogDetail


urlpatterns = patterns(
    '',
    url(r'^(?P<blog__slug>[\w-]+)/(?P<slug>[\w-]+)/$',
        cache_page(settings.OPPS_CACHE_EXPIRE)(PostBlogDetail.as_view()),
        name='blogpost-detail'),
    url(r'^(?P<blog__slug>[\w-]+)/$',
        cache_page(settings.OPPS_CACHE_EXPIRE)(PostBlogList.as_view()),
        name='blogpost-list'),
)
