from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Advert, Apartment, House, Customer, User
from .forms import ProfileForm


class AdvertListView(ListView):
    model = Advert
    paginate_by = 6
    template_name = 'main/advert_list.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.kwargs.get('category_slug'):
            queryset = queryset.filter(advert_category__category_slug=self.kwargs['category_slug']).order_by('-id')
        return queryset


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'main/advert_detail.html'


class ApartmentCreateView(CreateView):
    model = Apartment
    template_name = 'main/forms.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже квартиры"
        return context


class HouseCreateView(CreateView):
    model = House
    template_name = 'main/forms.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже дома"
        return context


class CustomerProfile(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'accounts/profile/profile.html'


class CustomerProfileUpdate(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/profile/forms.html'
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
    return render(request, 'index.html', {'turn_on_block': turn_on_block, 'text': text})
