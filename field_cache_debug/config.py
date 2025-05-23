from django.conf import settings

FIELD_CACHE_DEBUG = settings.FIELD_CACHE_DEBUG if hasattr(settings, 'FIELD_CACHE_DEBUG') else False
