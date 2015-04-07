"""
Django settings for DareToThink project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f4ph2!x(7tt4_%6$r&#72d$c6n^=so^p8@1$5e^7^fyh(3224z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'debug_toolbar',
    'DareToThink',
    'userprofile',
    'tinymce',
    'grappelli',
    'filebrowser',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
)

TEMPLATE_DIRS = (
    '/home/NuovoVesuvio/DareToThink/DareToThink/templates/',
    #'/home/NuovoVesuvio/DareToThink/blog/templates/'
    '/home/NuovoVesuvio/DareToThink/userprofile/templates/',
    '/home/NuovoVesuvio/DareToThink/DareToThink/templates/myadmin/',
)

#STATICFILES_DIRS = (
    #'home/NuovoVesuvio/DareToThink/DareToThink/static/',
    #'/static/',
    #os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
#)

STATICFILES_DIRS = (
    '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/',
    'home/NuovoVesuvio/profileimages/'
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'DareToThink.urls'

WSGI_APPLICATION = 'DareToThink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        #'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NuovoVesuvio$DareToThink2',
        'USER': 'NuovoVesuvio',
        'PASSWORD': 'secondDB',
        'HOST': 'mysql.server',
    }
}

#SOUTH_DATABASE_ADAPTERS = {
#    'default' : 'south.db.mysql'
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Accessing a users profile is done by calling user.get_profile(), but in order to use this function, Django needs to know where to look for the profile object.
#AUTH_PROFILE_MODULE = "userprofile.UserProfile"
LOGIN_URL = '/login/'

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
# allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    'django.core.context_processors.media',
]

AUTHENTICATION_BACKENDS = (

# Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

# `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",

)

#contrib.sites
SITE_ID = 1

#Allauth
LOGIN_REDIRECT_URL = '/profile'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

#TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
# 'django.template.loaders.app_directories.Loader',
# 'DareToThink.other.templateloader',
# )

#for this line in viewsblog.py: request.session['alpha'] = Comment.post
#SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TINYMCE_JS_URL = os.path.join(MEDIA_ROOT, "js/tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "js/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,image",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER=True