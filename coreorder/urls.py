from django.urls import path
from .views import OrderTypeView, OrderItemView

urlpatterns = [
    path("", OrderTypeView.as_view(), name="order_type_assignment_type"),
    path("paper-instructions/", OrderItemView.as_view(),
         name="order_item_instructions"),
]
