from django.urls import path, include
from rest_framework import routers

from apis.users.views import UserViewSet

router = routers.DefaultRouter()
router.register("", UserViewSet, basename='users')

urlpatterns = [
    path("", include(router.urls)),
]
