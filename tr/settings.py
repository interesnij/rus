import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'ur_4&s!%8!z+_60jrgh!%i7m14z%*h!v*!=1rpou5ebfb%$8jnfg00'


DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'rest_framework',
    'imagekit',
    'rest_framework.authtoken',
    'channels',
    'easy_thumbnails',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'rest_auth',
    'django_extensions',
    'goods',
    'users',
    'communities',
    'posts',
    'follows',
    'invitations',
    'moderation',
    'notifications',
    'main',
    'ckeditor',
    'ckeditor_uploader',
    'frends',
    'chat',
    'gallery',
    'article',
    'common',
]


SITE_ID = 1


CKEDITOR_CONFIGS = {
       'default': {
           'toolbar': 'full',
           'height': 500,
           'width': '100%',
           'removePlugins': 'stylesheetparser',
           'extraPlugins': ','.join(['youtube']),
       },
    }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'users.middleware.UpdateLastActivityMiddleware',
]

ROOT_URLCONF = 'tr.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]

WSGI_APPLICATION = 'tr.wsgi.application'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tr_db8',
        'USER': 'tr',
        'PASSWORD': 'DuhVremeni3',
        'HOST': 'localhost',
        'PORT': '5432',
    }
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')


REST_SESSION_LOGIN = True
REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'tr.serializers.RegisterSerializer',
}

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_ADAPTER = 'tr.adapter.MyAccountAdapter'
AUTH_USER_MODEL = 'users.User'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USERNAME_REQUIRED = False


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

UNICODE_JSON = True
REDIS_URL = "redis://127.0.0.1:6379"
ASGI_APPLICATION = 'tr.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL, ],
        },
    }
}

FIRSTNAME_MAX_LENGTH = 15
LASTNAME_MAX_LENGTH = 30
USER_MAX_FOLLOWS = 1500
USER_MAX_CONNECTIONS = 1500
USER_MAX_COMMUNITIES = 1000
POST_MAX_LENGTH = 5000
POST_COMMENT_MAX_LENGTH = 1500
COMMUNITY_NAME_MAX_LENGTH = 32
COMMUNITY_TITLE_MAX_LENGTH = 32
COMMUNITY_DESCRIPTION_MAX_LENGTH = 500
COMMUNITY_USER_ADJECTIVE_MAX_LENGTH = 16
COMMUNITY_USERS_ADJECTIVE_MAX_LENGTH = 16
COMMUNITY_RULES_MAX_LENGTH = 5000
COMMUNITY_CATEGORIES_MAX_AMOUNT = 3
COMMUNITY_CATEGORIES_MIN_AMOUNT = 1
COMMUNITY_AVATAR_MAX_SIZE = 10485760
COMMUNITY_COVER_MAX_SIZE = 10485760
TAG_NAME_MAX_LENGTH = 32
COMMUNITY_CATEGORY_NAME_MAX_LENGTH = 32
COMMUNITY_CATEGORY_TITLE_MAX_LENGTH = 64
COMMUNITY_CATEGORY_DESCRIPTION_MAX_LENGTH = 64
SEARCH_QUERIES_MAX_LENGTH = 120
MODERATION_REPORT_DESCRIPTION_MAX_LENGTH = 1000
MODERATED_OBJECT_DESCRIPTION_MAX_LENGTH = 1000
GLOBAL_HIDE_CONTENT_AFTER_REPORTS_AMOUNT = 20
MODERATORS_COMMUNITY_NAME = 'mods'
PROXY_BLACKLIST_DOMAIN_MAX_LENGTH = 150
POST_COMMENT_MAX_LENGTH = 1500
POST_MEDIA_MAX_SIZE = 10485760
POST_LINK_MAX_DOMAIN_LENGTH = 126
POST_MEDIA_MAX_ITEMS = 1
PASSWORD_MIN_LENGTH = 10
PASSWORD_MAX_LENGTH = 100
PROFILE_LOCATION_MAX_LENGTH = 64
PROFILE_BIO_MAX_LENGTH = 1000
PROFILE_AVATAR_MAX_SIZE = 10485760
PROFILE_COVER_MAX_SIZE = 10485760
PASSWORD_RESET_TIMEOUT_DAYS = 1


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True


THUMBNAIL_DEFAULT_OPTIONS = {"crop":"smart","detail":True}

THUMBNAIL_ALIASES = {
    "":{
        "avatar": {"size":(100,100)},
        "small_avatar": {"size":(60,60)},
    },
    "boom_shop":{
        "boom": {"size":(300,300)},
    },
    "floret_store":{
        "floret": {"size":(200,200)},
    },
    "faberlic":{
        "faberlic": {"size":(200,200)},
    },
    "goods2":{
        "goo": {"size":(350,450)},
    },
}
