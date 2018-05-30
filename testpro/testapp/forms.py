from django import forms
from .models import usermodel,log
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class usermodelform(forms.ModelForm):
    class Meta():
        model =  usermodel
        fields = ('site','profile_pic')

class tex(forms.ModelForm):
    class Meta():
        model  = log
        fields = ('text',)

                


