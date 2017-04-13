# -*- coding: utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'unxf*2p&b%m3^zfykm9j$ku@!u8j7(6!(#9v5d#f$7m@+#!h-g'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'expensas',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'consorcios.urls'

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
                "django.core.context_processors.media",
                "django.core.context_processors.static",
            ],
        },
    },
]

WSGI_APPLICATION = 'consorcios.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/media'
MEDIA_URL = "/media/"

TEMPLATES = [    
        {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',   
            'DIRS': [os.path.join(BASE_DIR, '/expensas/templates')],
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

# Configuración de Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'criscione',
        'USER': 'root',
        'PASSWORD': 'piculini',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Email Config
EMAIL_HOST = 'mx1.hostinger.com.ar'
EMAIL_HOST_USER = 'secretaria@criscioneyasociados.com.ar'
EMAIL_HOST_PASSWORD = 'secretariacriscione'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
