from django import forms
from .models import vote_model
from django.contrib.auth.models import User


class vote_form(forms.ModelForm):
    class Meta:
        model = vote_model
        fields = ('entrep',)

class registerUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)