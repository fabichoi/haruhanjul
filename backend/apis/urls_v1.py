from django.urls import path, include

version = "v1"

urlpatterns = [
    path(f"{version}/users/", include("apis.users.urls"))
]
