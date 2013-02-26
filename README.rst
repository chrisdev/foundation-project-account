==========================
foundation-project-account
==========================

A Django starter project based on `Zurb Foundation <http://foundation.zurb.com>`_

To Use ::

    export PROJECT_NAME=[your_project_name]
    mkvirtualenv $PROJECT_NAME && workon $PROJECT_NAME
    pip install Django<1.4
    mkdir $PROJECT_NAME
    django-admin.py startproject $PROJECT_NAME --template=https://github.com/justhamade/foundation-project-account/archive/master.zip $PROJECT_NAME
    cd $PROJECT_NAME
    pip install -r requirements.txt
    python manage.py syncdb --noinput
    python manage.py collectstatic --noinput

This project template provides :

 * apps folder for internal apps
 * initial data (for handling ``sites.Site`` model)
 * project requirements files for use with pip_
 * a home for your site static files
 * automatically compressed and minified JS, CSS and HTML via django-pipeline
 * basic templates designed to work with the foundation theme


Apps included:

 * django-debug-toolbar
 * django-pipeline
 * pinax-utils
 * pinax-theme-foundation
 * metron==0.1
 * django-user-accounts==1.0b3

.. _pip: http://www.pip-installer.org/
