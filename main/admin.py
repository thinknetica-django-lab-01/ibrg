from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage

from .models import Advert, Apartment, Category, House, Profile, Subscribe


def active(modeladmin, request, queryset):
    queryset.update(active=True)


def inactive(modeladmin, request, queryset):
    queryset.update(active=False)


active.short_description = 'Сделать активным(и)'
inactive.short_description = 'Сделать неактивным(и)'


class CkeditorFlatpageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())


class FlatPageAdmin(FlatPageAdmin):
    form = CkeditorFlatpageForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_title',)}


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('advert_title', 'price', 'area', 'rooms', 'advert_category', 'active',)
    list_filter = ('advert_category', 'created')
    prepopulated_fields = {'slug': ('advert_title',)}
    ordering = ('created',)
    actions = [active, inactive]


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Apartment)
admin.site.register(House)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Subscribe)
