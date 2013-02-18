# -*- coding: utf-8 -*-
# Django settings for basic pinax project.

import os.path
import posixpath
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG


INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"


STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "lts8n*nw7shur_4=q-c$ui!d(&!1$iagy3&tw2_ni#lnd-_*72"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "pipeline.middleware.MinifyHTMLMiddleware",
]

ROOT_URLCONF = "foundationtest.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "pinax_utils.context_processors.settings", 
    "account.context_processors.account",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    
    
    # theme
    "pinax_theme_foundation",
    
    # external
    "pipeline",
    "debug_toolbar",
    "metron",
 
     # project
    "account",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "what_next"
LOGOUT_REDIRECT_URLNAME = "home"

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass

PIPELINE_COMPILERS = (
)
PIPELINE_CSS = {
    "foundation": {
        "source_filenames": (
            "foundation/css/app.css",
            "foundation/css/foundation.css",
            "foundation/css/responsive-tables.css",
            "foundation/css/fc-webicons.css",
            "foundation/css/fonts/accessibility.css",
            "foundation/css/fonts/general_enclosed.css",
            "foundation/css/fonts/social.css",
            "foundation/css/fonts/general.css",
        ),
        "output_filename": "foundation.css",
    },
    "foundation_ie7": {
        "source_filenames": (
            "foundation/css/fonts/accessibility_ie7.css",
            "foundation/css/fonts/general_enclosed_ie7.css",
            "foundation/css/fonts/general_ie7.css",
            "foundation/css/fonts/social_ie7.css",
        ),
        "output_filename": "foundation_ie7.css",
    },
}

PIPELINE_JS = {
    "foundation": {
        "source_filenames": (
             "foundation/js/jquery.js",
             "foundation/js/jquery.foundation.mediaQueryToggle.js",
             "foundation/js/jquery.foundation.forms.js",
             "foundation/js/jquery.event.move.js",
             "foundation/js/jquery.event.swipe.js",
             "foundation/js/jquery.foundation.reveal.js",
             "foundation/js/jquery.foundation.orbit.js",
             "foundation/js/jquery.foundation.navigation.js",
             "foundation/js/jquery.foundation.buttons.js",
             "foundation/js/jquery.foundation.tabs.js",
             "foundation/js/jquery.foundation.tooltips.js",
             "foundation/js/jquery.foundation.accordion.js",
             "foundation/js/jquery.placeholder.js",
             "foundation/js/jquery.foundation.alerts.js",
             "foundation/js/jquery.foundation.topbar.js",
             "foundation/js/jquery.foundation.joyride.js",
             "foundation/js/jquery.foundation.clearing.js",
             "foundation/js/jquery.foundation.magellan.js",
             "foundation/js/responsive-tables.js",
             "foundation/js/app.js",
        ),
        "output_filename": "foundation.js",
    },
    "pinax": {
        "source_filenames": (
          "pinax/js/*.js",
        ),
        "output_filename": "pinax.js",
    }
}

