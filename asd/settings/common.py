import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = 'Replace me in production'

DEBUG = False

ALLOWED_HOSTS = ['*']

MAX_FILE_NUMBER = 100

SITE_URL = 'http://127.0.0.1:8000/'

INSTALLED_APPS = [
    'django_extensions',
    'compressor',
    'social_django',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'asd',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = SOCIAL_AUTH_LOGIN_ERROR_URL = LOGIN_URL = '/login/'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_ACCESS_TOKEN = ''

ROOT_URLCONF = 'asd.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'asd',
    }
}

COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = [
    ('text/less', 'node_modules/less/bin/lessc {infile} {outfile}'),
]

COMPRESS_SOURCE_ROOT = os.path.join(PROJECT_DIR, 'static')
COMPRESS_OUTPUT_DIR = 'cache'

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
BOWER_ROOT = os.path.join(PROJECT_DIR, 'static', 'bower_components')
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'media'))

COMPRESS_OFFLINE = False
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'debug': False
}

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    BOWER_ROOT,
]


WSGI_APPLICATION = 'asd.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True
