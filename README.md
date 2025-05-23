# django-field-cache-debug


### Installation

```
pip install git+ssh://github.com/ooppsss60/django-field-cache-debug.git
```

### Update settings
```
INSTALLED_APPS = [
    ...
    "field_cache_debug.apps.FieldCacheDebugConfig",
    ...
]
# Ignore admin site:
MIDDLEWARE = [
    ...
    "field_cache_debug.middlewares.SuppressFieldCacheWarningInAdminMiddleware",
    ...
]

FIELD_CACHE_DEBUG = True
```