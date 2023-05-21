from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm
from users.models import CustomUser


class SignUpView(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ro'yxatdan muvofaqqiyatli o'tdingiz")
            return redirect('users:login')

        else:
            form = RegisterForm(request.POST)
            return render(request, 'users/register.html', {'form': form})


class SignInView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Tizimga muvofaqqiyatli kirdingiz')
            return redirect('home')

        else:
            form = AuthenticationForm(data=request.POST)
            messages.info(request, "Noto'g'ri Username yoki parol!", extra_tags='danger')
            return render(request, 'users/login.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        return render(request, 'users/profile.html')


def logout_user(request):
    messages.success(request, "Tizimdan chiqdingiz")
    logout(request)
    return redirect('home')
