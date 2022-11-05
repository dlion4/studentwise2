from traceback import print_stack
from django.views.generic import View
from django.shortcuts import render, redirect


class OrderTypeMixin(View):
    model = None
    template_name = ''
    form_class = None

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        bound_form = self.form_class(request.POST)
        # print(bound_form)
        if bound_form.is_valid():
            instance = bound_form.save(commit=False)
            instance.student = self.model.objects.get(user=request.user)
            instance.save()
            bound_form.save()
            return redirect("order_item_instructions")
        else:
            print(bound_form.errors)
            return render(request, self.template_name, {"form": bound_form})


class OrderItemMixin(View):
    model = None
    template_name = ''
    form_class = None

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class}
        context.update({
            "order": self.model.objects.last()
        })
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order = self.model.objects.last()
            instance.save()
            form.save()
            return redirect("order-payment")
        context = {'form': form}
        print(form.errors)
        return render(request, self.template_name, context)
