import os
import datetime
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.vipsace.org', 'localhost']

# Application definition

INSTALLED_APPS = [
    'website',
    'portalapp',
    'library',
    'cloudinary',
    'raven.contrib.django.raven_compat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'admin_email_sender',
    'multiselectfield',

]
# 'django_imgur',
#     'easy_thumbnails',
#     'filer',
#     'mptt',
#     's3direct',

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'ace.urls'

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

WSGI_APPLICATION = 'ace.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Social Auth ------------->
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/portal'

# SOCIAL_AUTH_FACEBOOK_KEY = '331164980660704'
# SOCIAL_AUTH_FACEBOOK_SECRET = '5ab463efe87199548fe9dbb53ddb3ccf'

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = ['username', 'first_name', 'last_name', 'email']

# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['']
# SOCIAL_AUTH_BACKEND_ERROR_URL = '/portal/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/portal'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}
# <------------- Social Auth

# AWS S3 ------

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
S3DIRECT_REGION = os.environ.get('S3DIRECT_REGION')
AWS_QUERYSTRING_AUTH = False

S3DIRECT_DESTINATIONS = {
    'members': {
        # REQUIRED
        'key': 'members/',

        # OPTIONAL
        'auth': lambda u: u.is_staff,  # done later
        'allowed': ['image/jpeg', 'image/png', 'video/mp4', 'image/jpg'],
        'acl': 'public-read',
        'content_disposition': 'attachment',
        'content_length_range': (5000, 20000000)
    },
    'projects': {
        # REQUIRED
        'key': 'projects/',

        # OPTIONAL
        'auth': lambda u: u.is_staff,  # done later
        'allowed': ['image/jpeg', 'image/png', 'video/mp4', 'image/jpg'],
        'acl': 'public-read',
        'content_disposition': 'attachment',
        'content_length_range': (5000, 20000000)
    },
    'events': {
        # REQUIRED
        'key': 'events/',

        # OPTIONAL
        'auth': lambda u: u.is_staff,  # done later
        'allowed': ['image/jpeg', 'image/png', 'video/mp4', 'image/jpg'],
        'acl': 'public-read',
        'content_disposition': 'attachment',
        'content_length_range': (5000, 20000000)
    },

    'gallery': {
        # REQUIRED
        'key': 'gallery/',

        # OPTIONAL
        'auth': lambda u: u.is_staff,  # done later
        'allowed': ['image/jpeg', 'image/png', 'video/mp4', 'image/jpg'],
        'acl': 'public-read',
        'content_disposition': 'attachment',
        'content_length_range': (5000, 20000000)
    },

}


if not DEBUG:
    import dj_database_url

    DATABASES['default'] = dj_database_url.config()
    SOCIAL_AUTH_POSTGRES_JSONFIELD = True

# ACE Portal ---------->
from django.utils.timezone import get_current_timezone

tz = get_current_timezone()
SELECTION_START_DATE = tz.localize(datetime.datetime.strptime(os.environ.get('SELECTION_START_DATE'), "%d/%m/%Y"))
SELECTION_END_DATE = tz.localize(datetime.datetime.strptime(os.environ.get('SELECTION_END_DATE'), "%d/%m/%Y"))
# <---------- End ACE Portal
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

if not DEBUG:
    # Sentry
    RAVEN_CONFIG = {
        'dsn': 'https://16419383ac1243679009b0087c4eb652:c8cb0ea06f3f42e8848bc6908b313964@sentry.io/1259354',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
    }
    # SECURE_SSL_REDIRECT = True
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Heroku
    import dj_database_url

    DATABASES['default'] = dj_database_url.config()
    SOCIAL_AUTH_POSTGRES_JSONFIELD = True

# Email -------->
EMAIL_USE_TLS = True
EMAIL_DEFAULT_SENDER = os.environ.get('EMAIL_DEFAULT_SENDER')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

if 'sendgrid' in os.environ.get('EMAIL_CLIENT'):
    EMAIL_HOST = 'smtp.sendgrid.net'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
# <-------- End Email

# DjangoFiler -------->
FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'django_imgur.storage.ImgurStorage',
            # 'OPTIONS': {
            #     'location': '/path/to/media/filer',
            #     'base_url': '/media/filer/',
            # },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            # 'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'django_imgur.storage.ImgurStorage',
            # 'OPTIONS': {
            #     'location': '/path/to/media/filer_thumbnails',
            #     'base_url': '/media/filer_thumbnails/',
            # },
        },
    },
    'private': {
        'main': {
            'ENGINE': 'django_imgur.storage.ImgurStorage',
            # 'OPTIONS': {
            #     'location': '/path/to/smedia/filer',
            #     'base_url': '/smedia/filer/',
            # },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'django_imgur.storage.ImgurStorage',
            # 'OPTIONS': {
            #     'location': '/path/to/smedia/filer_thumbnails',
            #     'base_url': '/smedia/filer_thumbnails/',
            # },
        },
    },
}
# <-------- End DjangoFiler

# Imgur ------->
IMGUR_CONSUMER_ID = os.environ.get('IMGUR_CONSUMER_ID')
IMGUR_CONSUMER_SECRET = os.environ.get('IMGUR_CONSUMER_SECRET')
IMGUR_USERNAME = os.environ.get('IMGUR_USERNAME')
IMGUR_ACCESS_TOKEN = os.environ.get('IMGUR_ACCESS_TOKEN')
IMGUR_ACCESS_TOKEN_REFRESH = os.environ.get('IMGUR_ACCESS_TOKEN_REFRESH')
# <------- End Imgur