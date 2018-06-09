from django.contrib.auth.models import User
from .models import comments_feed,buy_model,foot_com
from django import forms
from django.core.validators import MaxValueValidator
from django.core import validators

def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering, 
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email')

class comment_form(forms.ModelForm):
    class Meta():
        widgets = { 'idea': forms.TextInput(attrs={'size': 80})}
        model = comments_feed
        fields = ('name','idea')

class buy_form(forms.ModelForm):
    class Meta():
        model = buy_model
        widgets = { 'address_Line1': forms.TextInput(attrs={'size': 80}),
        'address_Line2': forms.TextInput(attrs={'size': 80})}
        fields = ('name','product_name','phone_no','email','address_Line1','address_Line2','city','country')
        
class com_form(forms.ModelForm):
    class Meta():
        model = foot_com
        fields = ('com_foo',)

class register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords Don't Match..")   
