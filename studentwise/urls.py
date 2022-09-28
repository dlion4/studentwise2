from django.contrib import admin
from django.urls import path, include
from coreorder import urls as coreorder_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("order/", include(coreorder_urls))
]


if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
