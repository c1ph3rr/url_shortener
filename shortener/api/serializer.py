from rest_framework import serializers

from shortener.models import TinyModel


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinyModel
        fields = ['url', 'hash', 'short_url']
