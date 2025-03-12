from django.urls import path, include
from rest_framework import routers

from apis.quotes.views import QuoteViewSet

router = routers.DefaultRouter()
router.register("", QuoteViewSet, basename='quotes')

urlpatterns = [
    path("", include(router.urls)),
]
