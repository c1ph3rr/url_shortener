from django.db import models
from django.urls import reverse

# Create your models here.

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
        url = 'http://127.0.0.1:8000' + url
        return url 