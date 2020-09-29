from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from ..models import Stock, StockOrder


class StockMasterAddView(TemplateView):
    template = 'master_add_view.html'

    def get(self, request, **kwargs):
        master_stocks = Stock.objects.all()

        return render(
            request=request,
            template_name=self.template,
            context={
                'master_stocks': master_stocks
            }
        )
    def post(self, request, **kwargs):
        print(request.POST)

        # Stock = Stock.objects.update(
        #     quantity=request.POST.get('quantity')
        # )

        return redirect(reverse('master_view'))