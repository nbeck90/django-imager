from configurations import Settings
import os


class Base(Settings):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    USER_NAME = os.environ.get('USER')
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'imagerprofile',
        'imager_images',
        'registration',
        'sorl.thumbnail',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'imager.urls'
    WSGI_APPLICATION = 'imager.wsgi.application'
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/Los_Angeles'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'imager/static')
    ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    TEMPLATE_DIRS = [
        os.path.join(BASE_DIR, 'imager/templates'),
        os.path.join(BASE_DIR, 'imager_images/templates'),
        os.path.join(BASE_DIR, 'imagerprofile/templates')
    ]

    # Registration and Email settings
    ACCOUNT_ACTIVATION_DAYS = 7
    REGISTRATION_AUTO_LOGIN = True
    LOGIN_REDIRECT_URL = '/profile'
    LOGOUT_REDIRECT_URL = 'home'


class Dev(Base):

    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    USER_NAME = os.environ.get('USER')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_imager',
            'USER': USER_NAME,
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

    DEBUG = True
    TEMPLATE_DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class Prod(Base):
    import dj_database_url

    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    DATABASES = {'default': dj_database_url.config()}

    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    ### Config for sending emails via Gmail SMTP
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

    # Config for sending email via AWS SES
    # EMAIL_BACKEND = 'django_ses.SESBackend'
    # AWS_SES_REGION_NAME = 'us-west-2'
    # AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
    # AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
