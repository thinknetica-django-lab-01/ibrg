from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage

from .models import Advert, Apartment, Category, House, Profile


class CkeditorFlatpageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())

class FlatPageAdmin(FlatPageAdmin):
    form = CkeditorFlatpageForm

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {'category_slug':('category_title',)}


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Advert)
admin.site.register(Apartment)
admin.site.register(House)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)