from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Advert


class AdvertListView(ListView):
    model = Advert
    paginate_by = 4
    template_name = 'main/advert_list.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.kwargs.get('category_slug'):
            queryset = queryset.filter(advert_category__category_slug=self.kwargs['category_slug']).order_by('-id')

        return queryset




class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'main/advert_detail.html'


def index(request):
    turn_on_block = True
    text = 'Лаборатория Django-разработки от школы Thinknetica'

    return render(request, 'index.html', {'turn_on_block': turn_on_block, 'text':text})
