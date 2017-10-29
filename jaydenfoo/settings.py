#-*- coding: utf-8 -*-
"""
Django settings for jaydenfoo project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import tempfile
import os.path
import platform

if platform.node()=="bandwagonhost-vps-ubuntu":
    DEBUG = False
else:
    DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'keyinfo/secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()
    # SECRET_KEY = 'v6qkw03_b$3wmy**9c&)txnuj76)(+vj*rut+n$p4e2della)4'

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['jaydenfoo.com', '67.216.217.73', 'www.jaydenfoo.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'DjangoUeditor',
    'tools',
    'hitcount',
    'album',
    'easy_thumbnails',
    'wechat',
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

ROOT_URLCONF = 'jaydenfoo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'jaydenfoo.wsgi.application'

LOGIN_URL = 'login'
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if DEBUG:
    MYSQL_DB = 'mydata'
    MYSQL_USER = 'root'
    MYSQL_PASS = '1234'
    MYSQL_HOST = ''
    MYSQL_PORT = ''
else:
    with open(os.path.join(BASE_DIR, 'keyinfo/mysql_config.txt')) as f:
        MYSQL_DB = f.readline().strip()
        MYSQL_USER = f.readline().strip()
        MYSQL_PASS = f.readline().strip()
        MYSQL_HOST = ''
        MYSQL_PORT = ''


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': MYSQL_DB,
            'USER': MYSQL_USER,
            'PASSWORD': MYSQL_PASS,
            'HOST': MYSQL_HOST,
            'PORT': MYSQL_PORT,
        }
    }
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
DEFAULT_CHARSET = 'UTF-8'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_collect")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Email settings
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'icebrick@163.com'
EMAIL_HOST_PASSWORD = ''


#hitcout settings
HITCOUNT_KEEP_HIT_ACTIVE = {'days': 1}
HITCOUNT_HITS_PER_IP_LIMIT = 0  # unlimited
HITCOUNT_EXCLUDE_USER_GROUP = ()  # not used
HITCOUNT_KEEP_HIT_IN_DATABASE = {'seconds': 10}

# easy_thumbnails设置
THUMBNAIL_ALIASES = {
        '':{
            'avatar': {'size': (50,50), 'crop': True},
            },
        }

THUMBNAIL_DEBUG = True

