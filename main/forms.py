from django import forms

from django.core.exceptions import ValidationError

from .models import User, Customer


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField()
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError('Возраст должен быть 18 и старше')
        return age
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

   

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('profile_type', 'phone')
