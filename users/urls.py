from django.urls import path

from users.views import SignUpView, SignInView

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='login'),
]
