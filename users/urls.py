from django.urls import path

from users.views import SignUpView, SignInView, logout_user, ProfileView

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
