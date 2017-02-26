import os

from personal_site.settings_local import ALLOWED_HOSTS, SECRET_KEY  # noqa

from personal_site.settings_local import (
    DROPBOX_TOKEN, PHOTO_STORIES,
    THUMBNAIL_URLS_FILE, HOME_PAGE_CONTENT, GA_CODE,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ['PHOTO_STORIES'] = PHOTO_STORIES
os.environ['THUMBNAIL_URLS_FILE'] = THUMBNAIL_URLS_FILE
os.environ['DROPBOX_TOKEN'] = DROPBOX_TOKEN
os.environ['HOME_PAGE_CONTENT'] = HOME_PAGE_CONTENT
os.environ['GA_CODE'] = GA_CODE

DEBUG = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personal_site',
    'django_photo_stories',
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

ROOT_URLCONF = 'personal_site.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'personal_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

password_validation_module = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{}.UserAttributeSimilarityValidator'.format(
            password_validation_module,
        ),
    },
    {
        'NAME': '{}.MinimumLengthValidator'.format(
            password_validation_module,
        ),
    },
    {
        'NAME': '{}.CommonPasswordValidator'.format(
            password_validation_module,
        ),
    },
    {
        'NAME': '{}.NumericPasswordValidator'.format(
            password_validation_module,
        ),
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
