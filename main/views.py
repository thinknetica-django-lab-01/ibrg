from typing import Dict, Union

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.postgres.search import SearchVector

from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .forms import ProfileForm, SubscribeForm, UserForm
from .models import Advert, Apartment, House, User
from .permissions import RealtorPermissionMixin
from .serializers import AdvertSerializer


# Advert section
class AdvertListView(ListView):
    model = Advert
    paginate_by = 6

    def get_template_names(self):
        is_mobile = getattr(self.request, 'Mobile_Agent', False)

        if is_mobile:
            return 'mobile.html'
        return 'main/advert_list.html'

    def get_queryset(self) -> QuerySet[Advert]:
        queryset: 'QuerySet[Advert]' = cache.get('object_list')
        query = self.request.GET.get('query', '')
        if not queryset:
            queryset = self.model.objects.all()
            cache.set('object_list', queryset)
        if query:
            queryset = self.model.objects.annotate(
                search=SearchVector('advert_title', 'description'),
            ).filter(search=query)
        if self.kwargs.get('tag'):
            category = self.kwargs.get('tag')
            queryset = queryset.filter(
                advert_category__icontains=self.kwargs['tag'])
            cache.set(f'object_list_{category}', queryset)
        return queryset


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'main/advert_detail.html'

    def get(self, request: HttpRequest,
            *args: object,
            **kwargs: object) -> HttpResponse:
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        # send views value to context
        # for cache set name, object and time
        context['cache_views'] = cache.get_or_set(
            f'object_viewed_{self.object.pk}', self.object.views, 60)
        # save view counter
        self.object.views += 1
        self.object.save()
        return self.render_to_response(context)


class AdvertUpdate(RealtorPermissionMixin, UpdateView):
    model = Advert
    template_name = 'components/forms.html'
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs) -> Dict[str, object]:
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Изменения объявления"
        return context


class ApartmentCreateView(RealtorPermissionMixin, CreateView):
    model = Apartment
    template_name = 'components/forms.html'
    fields = '__all__'

    def get_context_data(self, **kwargs) -> Dict[str, object]:
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

    def get_context_data(self, **kwargs) -> Dict[str, object]:
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = "Новое объявление по продаже дома"
        return context


# Account section
@method_decorator(cache_page(60 * 5), name='dispatch')  # NEW
class Profile(LoginRequiredMixin, DetailView):
    template_name = 'account/profile/profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)


@login_required
def update_profile(request) -> HttpResponse:
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
    return render(request, 'index.html', {
        'turn_on_block': turn_on_block,
        'text': text})


@login_required()
def subscribe(request: HttpRequest) -> \
        Union[HttpResponseRedirect, HttpResponse]:
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


# API
class SmallResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 5


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.advert_owner == request.user


class AdvertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    pagination_class = SmallResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['advert_title', 'description', 'price']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
