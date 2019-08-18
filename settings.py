 # -*- coding:utf-8 -*-

"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to umap/settings/local.py. It should not be checked into
your code repository.

"""
from umap.settings.base import *   # pylint: disable=W0614,W0401

SECRET_KEY = 'secret'
INTERNAL_IPS = ('127.0.0.1', )

UMAP_DEMO_SITE = False
DEBUG = False

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'umap',
        'HOST': 'ip',
        'USER': 'umap',
        'PASSWORD': 'secret',
    }
}

INSTALLED_APPS += (
    # "django_extensions",
    # "debug_toolbar",
)


WSGI_APPLICATION = 'umap.wsgi.application'

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = True

# STATICFILES_DIRS = (
#     # os.path.join(PROJECT_DIR, 'remote_static'),
#     # "/home/ybon/Code/py/cartes.data.gouv.fr/static/",
#     #("storage", "/srv/umap/Code/js/Leaflet.Storage/"),
#     #("reqs", "/srv/umap/Code/js/Leaflet.Storage/reqs/"),
# ) + STATICFILES_DIRS

LANGUAGE_CODE = 'en'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
MIDDLEWARE += (
    'social_django.middleware.SocialAuthExceptionMiddleware',
)
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_BACKEND_ERROR_URL = "/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/"

# UMAP_DEMO_PK = 1
# UMAP_SHOWCASE_PK = 1373
LEAFLET_STORAGE_ALLOW_ANONYMOUS = True
# UMAP_DEMO_SITE = True
# TEMPLATES[0]['DIRS'].insert(0, '/home/ybon/Code/py/cartes.data.gouv.fr/templates/')

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'django.utils.log.NullHandler',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#             'level': 'DEBUG'
#         },
#         'mail_admins': {
#             'class': 'django.utils.log.AdminEmailHandler',
#             'level': 'WARNING',  # Don't mail below warning (info, etc)
#             'include_html': False
#         },
#     },
#     'formatters': {
#         'simple': {
#             'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#         },
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(funcName)s(...) [from %(pathname)s:%(lineno)s] %(message)s'
#         },
#     },
#     'loggers': {
#         # Empty string to get a catch-all logger
#         '': {
#             'handlers': ['mail_admins', 'console'],
#             'propagate': False,
#             'level': 'DEBUG',  # Log everything up to INFO (excludes DEBUG)
#         },
#         'django.request': {
#             'handlers': ['mail_admins', 'console'],
#             'level': 'ERROR',  # Will mail/print 5xx errors, but not 4xx
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'handlers': ['null'],  # Don't log django db stuff
#             'propagate': False,
#         },
#         'sesql': {
#             'handlers': ['console'],  # Don't log sesql stuff
#             'propagate': False,
#             'level': 'DEBUG',
#         },
#     }
# }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}
POSTGIS_VERSION = (2, 3, 0)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['*', ]
STATIC_SERVE = True
SOUTH_TESTS_MIGRATE = False
UMAP_USE_UNACCENT = True
STATIC_ROOT = '/srv/umap/static'
MEDIA_ROOT = '/srv/umap/uploads'
# LEAFLET_STORAGE_XSENDFILE_HEADER = 'X-Accel-Redirect'
# LEAFLET_ZOOM = 8
# LEAFLET_STORAGE_GZIP = False
LEAFLET_LONGITUDE = -95
LEAFLET_LATITUDE = 49
LEAFLET_ZOOM = 4

EBUG_STATIC_FINDER = True
UMAP_EXCLUDE_DEFAULT_MAPS = True
SITE_NAME = 'uMap'
ENABLE_ACCOUNT_LOGIN = True
