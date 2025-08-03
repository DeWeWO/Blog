from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from .models import User
from django.contrib.auth import login, login, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm


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
                form.add_error(None, "Username yoki email yoki parol noto‘g‘ri.")
        return redirect("login")
    