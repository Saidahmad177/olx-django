from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from ads.models import Ad
from users.forms import RegisterForm, ProfileForm
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


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')

    def post(self, request):
        form = ProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile malumotlari muvofaqqiyatli yangilandi")
            return redirect('users:profile')

        else:
            print(form.errors)
            return render(request, 'users/profile.html', {'form': form})


@login_required
def logout_user(request):
    messages.success(request, "Tizimdan chiqdingiz")
    logout(request)
    return redirect('home')


class UserAdsView(LoginRequiredMixin, View):
    def get(self, request):
        user_ads = Ad.objects.filter(user=request.user).order_by('-id')

        context = {
            'user_ads': user_ads,
        }

        return render(request, 'users/user_ads.html', context)


class ShowUserView(View):
    def get(self, request, id, username):
        user_id = CustomUser.objects.get(username=username)
        user_ads = Ad.objects.filter(user=id)
        search_result = 0

        search = request.GET.get('q', '')
        if search:
            search_result = user_ads.filter(title__icontains=search)
            context = {
                'user_id': user_id,
                'search_result': search_result,
            }
            return render(request, 'users/show_user_search.html', context)

        context = {
            'user_ads': user_ads,
            'user_id': user_id,
            'search_result': search_result,
        }

        return render(request, 'users/show_user.html', context)


