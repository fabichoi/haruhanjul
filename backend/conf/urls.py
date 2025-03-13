from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('swagger/', SpectacularSwaggerView.as_view(), name="swagger-ui"),
    path('', include("apis.urls")),
]
