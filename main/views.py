from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ProfileForm, SubscribeForm, UserForm
from .models import Advert, Apartment, House, User
from .permissions import RealtorPermissionMixin
from django.db.models import F

# Advert section

class AdvertListView(ListView):
    model = Advert
    paginate_by = 6
    template_name = 'main/advert_list.html'

    def get_queryset(self):
        queryset = cache.get('object_list')
        if not queryset:
            queryset = self.model.objects.all()
            cache.set('object_list', queryset)
        if self.kwargs.get('category_slug'):
            category = self.kwargs.get('category_slug')
            queryset = queryset.filter(advert_category__category_slug=self.kwargs['category_slug']).order_by('-id')
            cache.set(f'object_list_{category}', queryset)
        return queryset


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'main/advert_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        # send views value to context
        context['cache_views'] = cache.get_or_set(f'object_viewed_{self.object.pk}', self.object.views, 60)
        # save view counter
        self.object.views += 1
        self.object.save()

        return self.render_to_response(context)


class AdvertUpdate(RealtorPermissionMixin, UpdateView):
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


class ApartmentCreateView(RealtorPermissionMixin, CreateView):
    model = Apartment
    template_name = 'components/forms.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже квартиры"
        return context


class HouseCreateView(RealtorPermissionMixin, CreateView):
    model = House
    template_name = 'components/forms.html'
    fields = '__all__'
    permission_required = ('advert.can_add',)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Новое объявление по продаже дома"
        return context


# Account section
@method_decorator(cache_page(60 * 5), name='dispatch')  # NEW
class Profile(LoginRequiredMixin, DetailView):
    template_name = 'account/profile/profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
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


@login_required()
def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.active = True
            form.save()
            messages.info(request, 'Вы успешно добалены в спам-рассылку')
            return redirect('/')
    else:
        form = SubscribeForm()
    return render(request, 'main/subscribe.html', {'form': form})
