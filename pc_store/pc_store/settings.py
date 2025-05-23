import os 
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent 
SECRET_KEY = 'django-insecure-ck=&86-%5+lucylw73r7yl)h36-o0kww+c9*v#y#!x3q261%c0'
DEBUG = True 
ALLOWED_HOSTS = [] 
INSTALLED_APPS = [ 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'store',
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

ROOT_URLCONF = 'pc_store.urls' 

TEMPLATES = [ 
    { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [BASE_DIR / 'store/templates'],
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

WSGI_APPLICATION = 'pc_store.wsgi.application' 

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', 
    } 
}

AUTH_PASSWORD_VALIDATORS = [ 
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, 
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, 
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, 
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}, 
] 

LANGUAGE_CODE = 'ru' 
TIME_ZONE = 'Europe/Minsk' 
USE_I18N = True 
USE_L10N = True 
USE_TZ = True 

STATIC_URL = '/static/' 
STATICFILES_DIRS = [BASE_DIR / 'store/static']
MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR / 'media' 

LOGGING = { 
    'version': 1, 
    'disable_existing_loggers': False, 
    'handlers': { 
        'file': { 
            'level': 'DEBUG', 
            'class': 'logging.FileHandler', 
            'filename': BASE_DIR / 'debug.log', 
        }, 
    }, 
    'loggers': { 
        'django': { 
            'handlers': ['file'], 
            'level': 'DEBUG', 
            'propagate': True, 
        }, 
    }, 
} 
LOGOUT_REDIRECT_URL = 'index'
LOGIN_URL = 'login'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'guardmaximus4@gmail.com'         
EMAIL_HOST_PASSWORD = 'bnus odyr ursa czcv'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER