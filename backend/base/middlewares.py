import sentry_sdk
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponseForbidden


class SentryTransactionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        with sentry_sdk.start_transaction(op="http.request", name=request.path):
            response = self.get_response(request)
            return response


class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_countries = ["KR", ]

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', '')
        if ip == "127.0.0.1":
            return self.get_response(request)

        try:
            geo = GeoIP2()
            country_code = geo.country(ip)['country_code']
            if country_code not in self.allowed_countries:
                return HttpResponseForbidden("Access Denied: IP Blocked")
        except Exception:
            return HttpResponseForbidden("Access Denied: IP Blocked")

        return self.get_response(request)
