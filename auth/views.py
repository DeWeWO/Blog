from django.shortcuts import render
from .forms import LoginForm
from django.views import View


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "auth/login.html", {"form": form})