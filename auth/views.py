from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views import View
from .models import User
from django.contrib.auth import login, logout, authenticate, get_user_model


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "auth/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "auth/login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                print("User not found.!")
        return redirect("index")
    
class LogoutView(View):
    def get(self, request):
        logout(request=request)
        return redirect("index")