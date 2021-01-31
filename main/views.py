from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required

from .models import Advert, Apartment, House, Customer, User
from .forms import ProfileForm


class AdvertListView(ListView):
    model = Advert
    paginate_by = 10
    template_name = 'main/advert_list.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.kwargs.get('category_slug'):
            queryset = queryset.filter(advert_category__category_slug=self.kwargs['category_slug']).order_by('-id')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context.get('is_paginated', False):
            return context

        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number

        if num_pages <= 11 or page_no <= 6:  # case 1 and 2
            pages = [x for x in range(1, min(num_pages + 1, 12))]
        elif page_no > num_pages - 6:  # case 4
            pages = [x for x in range(num_pages - 10, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 5, page_no + 6)]

        context.update({'pages': pages})
        return context



class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'main/advert_detail.html'


class ApartmentCreateView(CreateView):
    model = Apartment
    template_name = 'main/forms.html'
    fields ='__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже квартиры"
        return context

class HouseCreateView(CreateView):
    model = House
    template_name = 'main/forms.html'
    fields ='__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже дома"
        return context

class CustomerProfileUpdate(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/profile/forms.html'
    # fields = ('first_name', 'last_name', 'email')
    success_url = '/'
    
    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)



class AdvertUpdate(UpdateView):
    model = Advert
    template_name = 'main/forms.html'
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Изменения объявления"
        return context



def index(request):
    turn_on_block = True
    text = 'Лаборатория Django-разработки от школы Thinknetica'

    return render(request, 'index.html', {'turn_on_block': turn_on_block, 'text':text})
