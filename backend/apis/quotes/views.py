import random

from django.db.models import Min, Max
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apis.exceptions import ApiValidationError
from apis.quotes.serializers import QuoteSerializer
from apps.quotes.models import Quote
from base.mixins import SentryLoggingMixin


class QuoteViewSet(
    SentryLoggingMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = QuoteSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def list(self, request, *args, **kwargs):
        min_id, max_id = Quote.objects.aggregate(Min('id'), Max('id')).values()

        if min_id is None or max_id is None:
            return Response(data={})

        idx = 0
        while max_id > idx:
            random_id = random.randint(min_id, max_id)
            quote = Quote.objects.filter(id=random_id).first()
            if quote:
                serializer = self.get_serializer(quote)
                return Response(data=serializer.data)
            idx += 1

        return Response(data={})

    @action(methods=["POST"], detail=True)
    def like(self, request, pk=None):
        if not pk:
            raise ApiValidationError()

        quote = Quote.objects.filter(id=pk).last()

        if not quote:
            raise ApiValidationError()

        quote.like_count += 1
        quote.save()
        return Response({"like_count": quote.like_count})
