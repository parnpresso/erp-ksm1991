from django.contrib import admin

from .models import Purchase, PurchaseStatus, PurchaseStock
from stocks.models import Stock


class StockAdmin(admin.TabularInline):
    model = PurchaseStock

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [StockAdmin, ]

    list_display = (
        'request_date',
        'purchase_date',
        'status',
        'noted',
    )
    list_filter = (
        'status',
    )
    search_fields = [
        'status',
    ]

@admin.register(PurchaseStatus)
class PurchaseStatusAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = (
        'name',
    )
    search_fields = [
        'name',
    ]
