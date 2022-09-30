from coreorder.forms.forms import OrderTypeForm, OrderItemForm
from .models import UserProfile
from coreorder.models import OrderType
from coreorder.store.viewmixins import OrderTypeMixin, OrderItemMixin


class OrderTypeView(OrderTypeMixin):
    model = UserProfile
    template_name = "coreorder/ordertype_form.html"
    form_class = OrderTypeForm

    

class OrderItemView(OrderItemMixin):
    model = OrderType
    form_class = OrderItemForm
    template_name = 'coreorder/orderitem_form.html'

    
