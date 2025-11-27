from django.http import HttpResponseForbidden
from django.conf import settings

class RestrictIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = getattr(settings, "ALLOWED_IPS", [])
        ip = request.META.get('REMOTE_ADDR')

        if ip not in allowed_ips:
            return HttpResponseForbidden("Access denied.")

        response = self.get_response(request)
        return response
