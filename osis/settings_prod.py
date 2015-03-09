from osis.settings import *

BASE_DIR = '/home/ps10comu/domains/ps10.com.ua/django/osis/'

SECRET_KEY = 'y2shfr99pqyltf#r@4h$@et^f@-=^-n2kkdf4(2+qc$a7y!d5u'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS += (
)

MIDDLEWARE_CLASSES += (
)

WSGI_APPLICATION = 'osis.wsgi_prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'config', 'mysql.config'),
        },
    }
}

STATIC_ROOT = '/home/ps10comu/domains/ps10.com.ua/public_html/static'

HONEYPOT_FIELD_NAME = 'phonenumber'
ENVELOPE_SUBJECT_INTRO = 'TEST'
ENVELOPE_EMAIL_RECIPIENTS = ['sale@ps10.com.ua']

EMAIL_HOST = 'mail.ps10.com.ua'
EMAIL_HOST_USER = 'sale@ps10.com.ua'
EMAIL_HOST_PASSWORD = 'hCmtnrzPPr7Q35'

SITE_ID = 1