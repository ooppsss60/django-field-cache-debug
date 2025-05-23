from django.apps import AppConfig



class FieldCacheDebugConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "field_cache_debug"

    def ready(self):
        from field_cache_debug import debug # NOQA
