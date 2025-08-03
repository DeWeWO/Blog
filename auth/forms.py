from django.contrib.auth.forms import UserCreationForm as BaseCreationForm, UserChangeForm as BaseChangeForm
from .models import User
from django import forms

class UserCreationForm(BaseCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "discipline", "user_group")

class UserChangeForm(BaseChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "discipline", "user_group")

class LoginForm(forms.Form):
    username_or_email = forms.CharField(required=True, max_length=255)
    password = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}))
