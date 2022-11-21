import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'django-insecure-)ez42jr6ux97)kg5s$^8kq-(p^sbay!u)or*akawt^+s$)-_o('

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True