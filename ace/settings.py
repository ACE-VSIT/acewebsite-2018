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

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'website',
    's3direct',
    'portalapp',
    'raven.contrib.django.raven_compat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

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

# FB Login

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/portal'

# SOCIAL_AUTH_FACEBOOK_KEY = '331164980660704'  # key for production
# SOCIAL_AUTH_FACEBOOK_SECRET = '5ab463efe87199548fe9dbb53ddb3ccf'  # secret for production

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')  # key for testing
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')  # secret for testing

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = ['username', 'first_name', 'last_name', 'email']

# SOCIAL_AUTH_BACKEND_ERROR_URL = '/portal/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/portal'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# AWS S3

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
S3DIRECT_REGION = os.environ.get('S3DIRECT_REGION')
AWS_QUERYSTRING_AUTH = False

# print(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, S3DIRECT_REGION)

# Destinations, with the following keys:
#
# key [required] Where to upload the file to, can be either:
#     1. '/' = Upload to root with the original filename.
#     2. 'some/path' = Upload to some/path with the original filename.
#     3. functionName = Pass a function and create your own path/filename.
# key_args [optional] Arguments to be passed to 'key' if it's a function.
# auth [optional] An ACL function to whether the current Django user can perform this action.
# allowed [optional] List of allowed MIME types.
# acl [optional] Give the object another ACL rather than 'public-read'.
# cache_control [optional] Cache control headers, eg 'max-age=2592000'.
# content_disposition [optional] Useful for sending files as attachments.
# bucket [optional] Specify a different bucket for this particular object.
# server_side_encryption [optional] Encryption headers for buckets that require it.

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
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.social_auth.associate_by_email',
# )

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}

if not DEBUG:
    import dj_database_url

    DATABASES['default'] = dj_database_url.config()
    SOCIAL_AUTH_POSTGRES_JSONFIELD = True

# Portal Start Date

SELECTION_START_DATE = datetime.datetime.strptime(os.environ.get('SELECTION_START_DATE'), "%d/%m/%Y").date()
SELECTION_END_DATE = datetime.datetime.strptime(os.environ.get('SELECTION_END_DATE'), "%d/%m/%Y").date()

# Sentry
if not DEBUG:
    RAVEN_CONFIG = {
        'dsn': 'https://16419383ac1243679009b0087c4eb652:c8cb0ea06f3f42e8848bc6908b313964@sentry.io/1259354',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
    }

