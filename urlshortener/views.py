from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Shortener

from .forms import ShortenerForm


def home_view(request):
    template = 'urlshortener/index.html'

    context = {}

    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url

            user_url = shortened_object.user_url

            context['new_url'] = new_url
            context['user_url'] = user_url

            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)

        shortener.visits += 1

        shortener.save()

        return HttpResponseRedirect(shortener.user_url)

    except:
        raise Http404('Something wen\'t wrong')