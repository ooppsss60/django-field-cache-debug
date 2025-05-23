from doctest import debug



class FieldCacheDebugConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from field_cache_debug import debug # NOQA
