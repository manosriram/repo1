from django import forms
from .models import vote_model


class vote_form(forms.ModelForm):
    class Meta:
        model = vote_model
        fields = ('entrep',)
