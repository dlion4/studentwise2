from django.shortcuts import render
from django.views.generic import View
from coreorder.forms.forms import OrderTypeForm
from django.http import HttpResponse
# Create your views here.


class OrderTypeView(View):

    template_name = "coreorder/ordertype_form.html"
    form_class = OrderTypeForm

    def get(self, request, **kwargs):
        context = {"form": self.form_class}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            instance = bound_form.save(commit=False)
            instance.save()
            bound_form.save()
            return HttpResponse("form saved")
        else:
            print(bound_form.errors)
            return render(request, self.template_name, {"form": bound_form})
