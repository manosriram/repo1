from django import forms
from django.contrib.auth.models import User
from .models import userProfile, imageModel


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class profileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ("bio", "interests")


class imageForm(forms.ModelForm):
    class Meta:
        model = imageModel
        fields = ('profile_pic',)
