from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Advert


class AdvertListView(ListView):
    model = Advert
    template_name = 'main/advert_list.html'


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'main/advert_detail.html'


def index(request):
    turn_on_block = True
    return render(request, 'index.html', {'turn_on_block': turn_on_block,})
