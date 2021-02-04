from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Advert, Apartment, House, User
from .forms import ProfileForm, UserForm

# Advert section
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

class AdvertUpdate(UpdateView):
    model = Advert
    template_name = 'components/forms.html'
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Изменения объявления"
        return context

class ApartmentCreateView(CreateView):
    model = Apartment
    template_name = 'components/forms.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже квартиры"
        return context


class HouseCreateView(CreateView):
    model = House
    template_name = 'components/forms.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже дома"
        return context


# Account section
class CustomerProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/profile/profile.html'


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(f'/accounts/profile/{request.user.id}/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)

    return render(request, 'components/forms.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



# base section
def index(request):
    turn_on_block = True
    text = 'Лаборатория Django-разработки от школы Thinknetica'
    return render(request, 'index.html', {'turn_on_block': turn_on_block, 'text': text})
