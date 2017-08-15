from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.shortcuts import resolve_url
from .models import ShortUrl

def show_view(request,**kwargs):
    print('show_viweee')
    short_url = get_object_or_404(ShortUrl,**kwargs)
    itens = ShortUrl.objects.all()
    ultimos = itens.order_by('-id')[:5]
    mais_acessadas = itens.order_by('-count')[:3]
    # print request.META
    return render(request,'shorted.html',locals())

def redirect_view(request,**kwargs):
    short_url = get_object_or_404(ShortUrl,**kwargs)
    short_url.count = short_url.count + 1
    ShortUrl.save(short_url)
    return redirect(short_url)

class ShortUrlCreateView(CreateView):
    model = ShortUrl
    fields = ['url']
    template_name = 'home.html'
    itens = ShortUrl.objects.all()
    print(itens)


    def get_queryset(self):
        return ShortUrl.objects

    def get_success_url(self):
        print('def  get success url')
        return resolve_url('shortener:url-preview',code=self.object.code)


