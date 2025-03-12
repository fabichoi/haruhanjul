from django.db import models

from base.models import AuditTimeStampModel


class Quote(AuditTimeStampModel):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    approved = models.BooleanField(default=False)


class Reference(AuditTimeStampModel):
    author = models.CharField(max_length=255)
    etc = models.CharField(max_length=255)