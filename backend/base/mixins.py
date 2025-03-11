import sentry_sdk
from django.conf import settings
from rest_framework.response import Response


class SentryLoggingMixin:
    def dispatch(self, request, *args, **kwargs):
        # 센트리 설정 없는 경우
        if not settings.USE_SENTRY:
            return super().dispatch(request, *args, **kwargs)

        with sentry_sdk.start_transaction(op="http.request", name=request.path):
            sentry_sdk.set_context("request_data", {
                "method": request.method,
                "query_params": request.GET.dict(),
                "post_data": request.POST.dict(),
                "headers": dict(request.headers),
                "user": request.user.id if request.user.is_authenticated else "Anonymous"
            })

            response = super().dispatch(request, *args, **kwargs)

            sentry_sdk.set_context("response_data", {
                "status_code": response.status_code,
                "data": response.data if isinstance(response, Response) else None
            })

            return response
