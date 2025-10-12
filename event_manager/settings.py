"""
Django settings for event_manager project.
... (Boilerplate content) ...
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# ...

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d5%*^!@^t_6(m+5#=r$h4^1yv8)81-&r!h8&g!j)7v&m#*g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # My Apps (Workaround for checker)
    'accounts',
    'events',
]

# FIX: Ensure all required MIDDLEWARE items are present
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # <-- E410 Fix
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <-- E408 Fix
    'django.contrib.messages.middleware.MessageMiddleware', # <-- E409 Fix
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_manager.urls'

# FIX: Ensure TEMPLATES configuration is present
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # <-- E403 Fix
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

WSGI_APPLICATION = 'event_manager.wsgi.application'


# ... (Database configuration and Password validation) ...

# Default primary key field type (Optional warning fix)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'
