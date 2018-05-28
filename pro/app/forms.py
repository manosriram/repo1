from django.contrib.auth.models import User
from django import forms
from .models import profile

class userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class profileform(forms.ModelForm):
    class Meta():
        model = profile
        fields = ('site','profile_pic')