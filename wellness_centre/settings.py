import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-django-secret-key')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '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')






DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# FIXED: Removed https:// and trailing slash
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'wellnesscentrewithai-production.up.railway.app']

# Also add .railway.app wildcard to accept any Railway subdomain
if not DEBUG:
    ALLOWED_HOSTS.append('.railway.app')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wellness_centre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'wellness_centre.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Changed to simpler storage for debugging
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

# For debugging - print to Railway logs
print(f"DEBUG: ALLOWED_HOSTS = {ALLOWED_HOSTS}")
print(f"DEBUG: Using static storage: {STATICFILES_STORAGE}")