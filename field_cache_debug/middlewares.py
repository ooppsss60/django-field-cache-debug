import warnings
from django.utils.deprecation import MiddlewareMixin

from field_cache_debug.warnings import FieldCacheWarning


class SuppressFieldCacheWarningInAdminMiddleware(MiddlewareMixin):

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", FieldCacheWarning)
                response = self.get_response(request)
        else:
            response = self.get_response(request)
        return response
