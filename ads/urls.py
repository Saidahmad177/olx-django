from django.urls import path
from .views import CreateAd

app_name = 'ads'
urlpatterns = [
    path('post-new-add/', CreateAd.as_view(), name='create'),
]
