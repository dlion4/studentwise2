from django import forms
from coreorder.models import OrderType, OrderItem


class OrderTypeForm(forms.ModelForm):
    class Meta:
        model = OrderType
        exclude = ['student']


class OrderItemForm(forms.ModelForm):
    progress_update = forms.CharField(widget=forms.CheckboxInput(attrs={

    }))
    sources_copy = forms.CharField(widget=forms.CheckboxInput(attrs={

    }))
    outline = forms.CharField(widget=forms.CheckboxInput(attrs={

    }))
    info_graph = forms.CharField(widget=forms.CheckboxInput(attrs={

    }))
    page_abstract = forms.CharField(widget=forms.CheckboxInput(attrs={

    }))
    page_summary = forms.CharField(widget=forms.CheckboxInput(attrs={

    }))

    class Meta:
        model = OrderItem
        exclude = ['order']
