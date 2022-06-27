from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
base_url = getattr(settings, 'ALLOWED_HOSTS')[0]

class TinyModel(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=200, unique=True)
    alias = models.CharField(max_length=200, null=True, blank=True)
    short_url = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    def get_url(self):
        url = reverse('redirect', kwargs={'hash': self.hash})
        url = base_url + url
        return url 