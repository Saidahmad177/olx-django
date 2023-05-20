from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from olx.views import HomePageView, SearchPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ads/', include('ads.urls')),
    path('users/', include('users.urls')),
    path('search/', SearchPageView.as_view(), name='search'),

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
