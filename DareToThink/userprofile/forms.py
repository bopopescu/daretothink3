from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'hello',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


        #username = forms.TextInput(attrs={'class':'form-group'})
        #for field in fields:
        #    field = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))

        #help_texts = {
        #'username': 'hello',
        #}


   # myfield = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


