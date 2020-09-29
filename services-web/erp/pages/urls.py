from django.urls import path

from .views.home_view import HomeView


urlpatterns = [
    path(
        route='',
        view=HomeView.as_view(),
        name='home_views'
    ),
]