from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from ..models import Stock, StockOrder


class StockEditView(TemplateView):
    template = 'edit_view.html'

    def get(self, request, id, **kwargs):
        transaction = StockOrder.objects.filter(id=id).first()

        return render(
            request=request,
            template_name=self.template,
            context={
                'transaction': transaction
            }
        )

    def post(self, request, id, **kwargs):
        print(request.POST)

        stock_order = StockOrder.objects.filter(id=id).update(
            quantity=request.POST.get('quantity')
        )

        return redirect(reverse('stock_list'))