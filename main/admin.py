from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import  FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget


from .models import Advert, Apartment, House



class CkeditorFlatpageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())

class FlatPageAdmin(FlatPageAdmin):
    form = CkeditorFlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Advert)
admin.site.register(Apartment)
admin.site.register(House)
