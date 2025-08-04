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
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)
    discipline = forms.CharField(required=False, max_length=255)
    user_group = forms.CharField(required=False, max_length=100)
    department = forms.CharField(required=False, max_length=100)
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "role", "department", "discipline", "user_group", "password1", "password2")
    
    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.role = self.cleaned_data["role"]
        
        # Role'ga qarab tegishli ma'lumotlarni to‘ldirish
        if user.role == 'student':
            user.discipline = self.cleaned_data.get("discipline")
            user.user_group = self.cleaned_data.get("user_group")
            user.department = None  # o‘qituvchi emas, shuning uchun bo‘sh
        elif user.role == 'teacher':
            user.department = self.cleaned_data.get("department")
            user.discipline = None
            user.user_group = None
        if commit:
            user.save()
        return user