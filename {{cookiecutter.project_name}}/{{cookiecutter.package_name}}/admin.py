#!/usr/bin/env python
"""
    {{ cookiecutter.package_name }}.admin
    ==========

    Admin Functionality for Blog App

"""
from django.contrib import admin

from blog.models import Example


class {{ cookiecutter.package_classname }}Admin(admin.ModelAdmin):
    # Display on {{ cookiecutter.package_classname }} App Admin list page
    # ===================================
    # list_display = ["title", "updated_at", "published"]
    # list_editable = ["published"]  # editable on the list page
    # list_filter = ["published", "updated_at", "author"]  # which filter should appear on list page.
    # For filtering/searching admin list page.
    # list_display_links = ["title"]  # which fields should link to 'change' page
    # Set date_hierarchy to the name of a DateField or DateTimeField in your model,
    # and the change list page will include a date-based drilldown navigation by that field.
    # date_hierarchy = "created_at"
    # Set search_fields to enable a search box on the admin change list page.
    # This should be set to a list of field names that will be searched whenever
    # somebody submits a search query in that text box.
    # search_fields = ["title", "content"]
    # {{ cookiecutter.package_classname }} App Admin App page
    # =======================
    # Set prepopulated_fields to a dictionary mapping field names to the fields it should prepopulate from
    # prepopulated_fields = {"slug": ("title",)}
    # Changes the 'add' or 'change' forms - e.g. if you want a simple add post in the admin
    # fields = ("published", "slug")
    pass

admin.site.register(Example, {{ cookiecutter.package_classname }}Admin)
