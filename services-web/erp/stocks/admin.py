from django.contrib import admin

from .models import Stock


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
