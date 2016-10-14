
.. image:: https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif
   :target: http://www.djangoproject.com/

.. image:: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/tree/master.svg?style=svg
   :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/tree/master


{{ cookiecutter.project_name }}
===============================
{{ cookiecutter.project_long_description }}

The documentation can be found at (once deployed): https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_name }}/ 


Getting Started
===============

If you're new to {{ cookiecutter.project_name }}, you may want to here to get
you up and running:


Installation
------------
Install via setuptools:

.. code-block:: console
    
    python setup.py install

Django 's Configuration
-----------------------
Add ``{{ cookiecutter.package_name }}`` to your configuration file (normally settings.py): 

.. code-block:: python

   INSTALLED_APPS =  [
    ...
    '{{ cookiecutter.package_name }}',
    ...
   ]


urls.py

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^accounts/', include('allauth.urls')),
        ...
    ]


Post-Installation
-----------------

In your Django root execute the command below to create your database tables::

    ./manage.py migrate