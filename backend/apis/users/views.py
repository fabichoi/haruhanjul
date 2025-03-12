from rest_framework.viewsets import ModelViewSet

from apis.users.serializers import UserSerializer
from apps.users.models import User
from base.mixins import SentryLoggingMixin


class UserViewSet(SentryLoggingMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
