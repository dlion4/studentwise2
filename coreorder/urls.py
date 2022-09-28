from django.urls import path
from .views import OrderTypeView

urlpatterns = [
    path("", OrderTypeView.as_view(), name="ordetype_assignment_type"),
]
