from django.urls import path
from .views import CreateAd, DetailAdView, CategoryItems

app_name = 'ads'
urlpatterns = [
    path('post-new-add/', CreateAd.as_view(), name='create'),
    path('<str:category>/', CategoryItems.as_view(), name='category'),
    path('<slug:category>/<slug:slug>/', DetailAdView.as_view(), name='detail'),
]
