from django import forms

from .models import User, Customer


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('profile_type', 'phone')
