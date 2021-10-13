from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from homepage.views import (
    homepage
)


urlpatterns = [
    path('', homepage, name="homepage"),
    path('cars/', include("cars.urls")),
    path('user_account/', include("user_account.urls")),
    path('user_contact/', include("user_contact.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
