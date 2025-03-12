from django.db import models


class Quote(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    approved = models.BooleanField(default=False)
