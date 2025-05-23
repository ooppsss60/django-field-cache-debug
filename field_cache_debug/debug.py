import warnings
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor

from field_cache_debug import config
from field_cache_debug.warnings import FieldCacheWarning


def check_field_cache(obj, field: str, stacklevel=2):
    if field not in obj._state.fields_cache:
        warnings.warn(
            message=f'Field "{field}" is missing in cache "{type(obj)}"',
            category=FieldCacheWarning,
            stacklevel=stacklevel
        )


def get_object(self, instance):
    check_field_cache(instance, self.field.name, 4)
    qs = self.get_queryset(instance=instance)
    # Assuming the database enforces foreign keys, this won't fail.
    return qs.get(self.field.get_reverse_related_filter(instance))


if config.FIELD_CACHE_DEBUG:
    ForwardManyToOneDescriptor.get_object = get_object
