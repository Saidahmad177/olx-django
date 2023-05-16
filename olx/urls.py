from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from olx.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ads/', include('ads.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
