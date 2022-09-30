import imp
from django.urls import path
from .views import homepage, paymenthandler

urlpatterns = [
    path("", homepage, name="order-payment"),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
]
