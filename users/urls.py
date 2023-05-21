from django.urls import path

from users.views import SignUpView, SignInView, logout_user, ProfileView, UserAdsView, ShowUserView

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('my-ads/', UserAdsView.as_view(), name='my-ads'),
    path('show/<int:id>-<str:username>/', ShowUserView.as_view(), name='show_user'),
]
