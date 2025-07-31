from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("first_name", "last_name", "username", "discipline", "user_group", "is_staff", "is_active",)
    list_filter = ("username", "discipline", "user_group", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "username", "discipline", "user_group", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "username", "discipline", "user_group", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username", "discipline", "user_group",)
    ordering = ("username", "discipline", "user_group",)

