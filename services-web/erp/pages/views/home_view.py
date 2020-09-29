from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template = 'home_view.html'

    def get(self, request, **kwargs):

        return render(
            request=request,
            template_name=self.template,
        )