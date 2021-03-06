from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from .models import TinyModel
from .forms import TinyForm
from .utils import Base62

# Create your views here.


def index(request):
    base62 = Base62()
    base_url = 'http://' + request.META['HTTP_HOST'] + '/'

    if request.method == 'POST':
        form = TinyForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            alias = form.cleaned_data['alias']

            model = TinyModel.objects.filter(url=url)
            if model:
                return render(request, 'shortener/index.html', {
                    'form': form,
                    'model': model[0]
                })
            elif alias:
                model = TinyModel.objects.create(url=url, hash=alias, alias=alias, short_url=base_url+alias)
                model.save()
                return render(request, 'shortener/index.html', {
                    'form': form,
                    'model': model
                })
            else:
                try:
                    latest_id = TinyModel.objects.latest('id')
                    hash = base62.encode_url(latest_id.id)
                except:
                    hash = base62.encode_url(0)

                model = TinyModel.objects.create(url=url, hash=hash, short_url=base_url+hash)
                model.save()
                return render(request, 'shortener/index.html', {
                    'form': form,
                    'model': model
                })
    else:
        form = TinyForm()
        return render(request, 'shortener/index.html', {
            'form': form
        })


def redirect(request, hash):
    try:
        model = TinyModel.objects.get(hash=hash)
        return HttpResponseRedirect(model.url)
    except:
        raise Http404
