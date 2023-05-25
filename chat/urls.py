from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('<int:receiver_id>/', views.room2, name='room2'),
    path('send', views.send, name='send'),
    path('<int:receiver_id>/check/', views.checkview2, name='checkview2'),
    path('getMessages2/<int:receiver_id>/', views.getMessages2, name='getMessages2'),
]
