from django import forms
from django.core.exceptions import ValidationError

from .models import Profile, User, Subscribe


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField()
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError('Возраст должен быть 18 и старше')
        return age
    
    class Meta:
        model = Profile
        fields = ('profile_type', 'phone')



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        exclude = ('user',)
