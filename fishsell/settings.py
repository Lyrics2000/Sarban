

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1=y5q)niwp$ve%1ywl)j&l!$rwtoo-twd&aunswp1z!v^&t3xq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['sleepy-savannah-28536.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'accounts',
    'addresses',
    'carts',
    'orders',
    'search',
    'billing',
    'mpesa',
    'storages',
    'contacts'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'fishsell.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'product/templates'),
            os.path.join(BASE_DIR,'carts/templates'),
            os.path.join(BASE_DIR,'search/templates'),
         os.path.join(BASE_DIR,'accounts/templates'),
         os.path.join(BASE_DIR,'addresses/templates'),
         os.path.join(BASE_DIR,'mpesa/templates'),
         os.path.join(BASE_DIR,'contacts/templates'),
         
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

WSGI_APPLICATION = 'fishsell.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST' : 'ec2-107-20-104-234.compute-1.amazonaws.com',
        'NAME' :'db0e40oghro5ea',
        'USER' : 'bnezixmerlgdsv',
        'PORT'  : 5432,
        'PASSWORD' : 'a629fa0212d23bf4cc9f63e7ae30e1c36596d1d85dcbd2441c1796f5bb670969',
    }
}

# # development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGOUT_REDIRECT_URL = '/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# #development
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'static_project_file'),
# ]
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_cdn')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'media_cdn')


#Email backends
EMIAL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'ambetsaachongo@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'Lyrics254'


#Production
AWS_ACCESS_KEY_ID = 'AKIA3T7FB5INOG27IH5T'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'handlings254'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_project_file'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'fishsell.storage_backends.MediaStorage' 







