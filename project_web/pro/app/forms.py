from django import forms
from django.contrib.auth.models import User
from .models import comments_feed

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email')

class comment_form(forms.ModelForm):
    class Meta():
        widgets = { 'comment': forms.TextInput(attrs={'size': 80})}
        model = comments_feed
        fields = ('name','comment')
