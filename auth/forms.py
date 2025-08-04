from django.contrib.auth.forms import UserCreationForm as BaseCreationForm, UserChangeForm as BaseChangeForm
from .models import User
from django import forms

class UserCreationForm(BaseCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "discipline", "user_group")

class UserChangeForm(BaseChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "discipline", "user_group")

class LoginForm(forms.Form):
    username_or_email = forms.CharField(required=True, max_length=255)
    password = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, max_length=100)
    discipline = forms.CharField(required=True, max_length=255)
    user_group = forms.CharField(required=True, max_length=100)
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "discipline", "user_group", "password1", "password2")
    
    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.discipline = self.cleaned_data["discipline"]
        user.user_group = self.cleaned_data["user_group"]
        if commit:
            user.save()
        return user