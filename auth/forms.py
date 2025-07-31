from django.contrib.auth.forms import UserCreationForm as BaseCreationForm, UserChangeForm as BaseChangeForm
from .models import User

class UserCreationForm(BaseCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "discipline", "user_group")

class UserChangeForm(BaseChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "discipline", "user_group")
