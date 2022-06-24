from django.http import Http404, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shortener.models import TinyModel
from .serializer import UrlSerializer
from shortener.utils import Base62


class CreateUrl(APIView):
    def __init__(self):
        self.base62 = Base62()

    def post(self, request, format=None):
        try:
            url = request.data['url']
            model = TinyModel.objects.filter(url=url)
            if model:
                serializer = UrlSerializer(model[0], many=False)
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                try:
                    latest_id = TinyModel.objects.latest('id')
                    hash = self.base62.encode_url(latest_id.id)
                except:
                    hash = self.base62.encode_url(0)
                
                base_url = 'http://' + request.META['HTTP_HOST'] + '/api/'
                model = TinyModel.objects.create(url=url, hash=hash, short_url=base_url+hash)
                serializer = UrlSerializer(model, many=False)
                return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response(f'Error: {e}', status.HTTP_400_BAD_REQUEST)


class RedirectUrl(APIView):
    def get_object(self, hash):
        try:
            return TinyModel.objects.get(hash=hash)
        except TinyModel.DoesNotExist:
            raise Http404

    def get(self, request,  hash):
        model = self.get_object(hash)
        return HttpResponseRedirect(model.url)
