from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from ..models import Stock


class StockListView(TemplateView):
    template = 'list_view.html'

    def get(self, request, **kwargs):
        stocks = Stock.objects.all()

        return render(
            request=request,
            template_name=self.template,
        )