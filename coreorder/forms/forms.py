from django import forms
from coreorder.models import OrderType, OrderItem


class OrderTypeForm(forms.ModelForm):
    class Meta:
        model = OrderType
        exclude = ['student', 'prices']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ['order']
