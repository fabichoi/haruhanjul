from django.urls import path, include

version = "v1"

urlpatterns = [
    path(f"{version}/users/", include("apis.users.urls")),
    path(f"{version}/quotes/", include("apis.quotes.urls")),
]
