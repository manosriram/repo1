from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core import validators
from .models import post


class register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
            if password != confirm_password:
                raise forms.ValidationError("Passwords Don't Match..")

class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = ('text','nick_name')
