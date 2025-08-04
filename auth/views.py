from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views import View
from .models import User
from django.contrib.auth import login, logout, authenticate, get_user_model


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "auth/register.html", {"form": form})
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            if login_user is not None:
                login(request, login_user)
                return redirect("index")
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
            # Avval email orqali user topishga harakat qilamiz
            try:
                user_obj = User.objects.get(email=username_or_email)
                username = user_obj.username  # foydalanuvchining username ni olamiz
            except User.DoesNotExist:
                username = username_or_email  # agar email topilmasa, bu username deb qaraymiz
            # Auth qilish
            user = authenticate(request, username=username, password=password)
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