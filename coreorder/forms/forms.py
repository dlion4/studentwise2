from django import forms
from coreorder.models import OrderType


class OrderTypeForm(forms.ModelForm):
    class Meta:
        model = OrderType
        fields = "__all__"
