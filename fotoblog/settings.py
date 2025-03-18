"""
Django settings for fotoblog project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(ri&tpq5)w1(s280_l9nz0-)ixhmod7py*3+!b%_d42at-upxq'

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
    'authentication',
    'blog',
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

ROOT_URLCONF = 'fotoblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
        ],
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

WSGI_APPLICATION = 'fotoblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 3,
        }
    },
    # {
        # 'NAME': 'authentication.validators.ContainsLetterValidator',        doit contenir au moins une lettre majuscule ou minuscule.
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',         ne peut pas trop ressembler à vos autres informations personnelles.
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',         ne peut pas être un mot de passe couramment utilisé.
    # 
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'authentication.validators.ContainsNumberValidator', 
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'authentication.User'

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = LOGIN_URL


MEDIA_URL = '/media/'   
# Premièrement,  MEDIA_URL  , qui est l’URL depuis laquelle Django va essayer de servir des médias. 
# Dans certains cas, ce peut être une URL complète vers un autre hôte, si vous utilisez un service tiers pour servir vos médias.
MEDIA_ROOT = BASE_DIR.joinpath('media/')
# Le deuxième paramètre à configurer est  MEDIA_ROOT. Il indique le répertoire local dans 
# lequel Django doit sauvegarder les images téléversées.


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Paramètres pour l'envoi d'e-mails via Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shileiwei200@gmail.com'
EMAIL_HOST_PASSWORD = 'gfimpmiubktrryum'


# Supprime la ligne "EMAIL_BACKEND = console" (si existante)

# Adresse email par défaut pour l'expéditeur
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
