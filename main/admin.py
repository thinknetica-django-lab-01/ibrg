from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import  FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget


from .models import Advert, Apartment, House, Category, Profile



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