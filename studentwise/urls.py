from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from coreorder import urls as coreorder_urls
from payment import urls as payment_urls
from django.conf import settings
from django.conf.urls.static import static


def homepage(request):
    return redirect("order_type_assignment_type")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("order/", include(coreorder_urls)),
    path('payment/', include(payment_urls)),
    path("", homepage)
]

if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
