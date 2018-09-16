from django import forms
from django.contrib.auth.models import User
from .models import profileUser


class registerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User,
        fields = ('username', 'email', 'password')


class profileForm(forms.ModelForm):
    class Meta():
        model = profileUser,
        fields = ('profilePic',)
