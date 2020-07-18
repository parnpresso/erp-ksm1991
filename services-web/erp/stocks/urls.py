from django.urls import path

from .views.list_view import StockListView


urlpatterns = [
    path(
        route='',
        view=StockListView.as_view(),
        name='stock_list'
    ),
]