from django.contrib import admin

from .models import Stock, StockOrder


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'volume',
        'unit',
        'size',
        'brand',
        'color',
        'created_date',
    )
    list_filter = (
        'sku',
        'name',
    )
    search_fields = [
        'sku',
        'name',
    ]

@admin.register(StockOrder)
class StockOrderAdmin(admin.ModelAdmin):
    list_display = (
        'stock',
        'quantity',
    )
    list_filter = (
        'stock',
        'quantity',
    )
    search_fields = [
        'stock',
        'quantity',
    ]
