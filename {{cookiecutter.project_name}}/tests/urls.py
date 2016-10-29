#!/usr/bin/env python
"""
    tests.urls
    ==========

    URLs for testing purposes ONLY

"""
from django.conf.urls import patterns, include, url

from {{ cookiecutter.package_name }} import urls as urls_{{ cookiecutter.package_name }}


urlpatterns = patterns('',
    url(r'^{{ cookiecutter.package_name }}/', include(urls_{{ cookiecutter.package_name }}, namespace="{{ cookiecutter.package_name }}")),
)
