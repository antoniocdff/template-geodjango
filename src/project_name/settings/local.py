from .base import *

INSTALLED_APPS += ('debug_toolbar',
                   'django_extensions', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

SECRET_KEY="oi"