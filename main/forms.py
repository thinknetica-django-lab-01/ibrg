from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError


from .models import User, Profile


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



# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('city', 'country') #Note that we didn't mention user field here.
#
#     def save(self, user=None):
#         user_profile = super(UserProfileForm, self).save(commit=False)
#         if user:
#             user_profile.user = user
#         user_profile.save()
#         return user_profile