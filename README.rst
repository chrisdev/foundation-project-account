==========================
foundation-project-account
==========================

A Django starter project based on `Zurb Foundation <http://foundation.zurb.com>`_

To Use ::

    $ django-admin.py startproject [your_project_name] --template=https://github.com/justhamade/foundation-project-account/archive/master.zip
    $ cd [your_project_name]
    $ mkvirtualenv [your_project_name] && workon [your_project_name]
    $ pip install -r requirements.txt

This project template provides :

 * apps folder for internal apps
 * initial data (for handling ``sites.Site`` model)
 * project requirements files for use with pip_
 * a home for your site static files
 * basic templates designed to work with the foundation theme


Apps included:

 * django-debug-toolbar
 * django-pipeline
 * pinax-utils
 * pinax-theme-foundation
 * metron==0.1
 * django-user-accounts==1.0b3

.. _pip: http://www.pip-installer.org/
