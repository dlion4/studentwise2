from django.db import models
from coreorder.models import OrderItem
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    order = models.OneToOneField(OrderItem,
                                 on_delete=models.SET_NULL, blank=True, null=True, related_name="order_payment")
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.order.prices


class Refund(models.Model):
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"
