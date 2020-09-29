from django.urls import path

from .views.list_view import StockListView
from .views.edit_view import StockEditView
from .views.master_view import StockMasterView
from .views.master_add_view import StockMasterAddView


urlpatterns = [
    path(
        route='',
        view=StockListView.as_view(),
        name='stock_list'
    ),
    path(
        route='<int:id>/edit',
        view=StockEditView.as_view(),
        name='stock_edit',
    ),
    path(
        route='master',
        view=StockMasterView.as_view(),
        name='master_view',
    ),
        path(
        route='masteradd',
        view=StockMasterAddView.as_view(),
        name='master_add_view',
    )
]