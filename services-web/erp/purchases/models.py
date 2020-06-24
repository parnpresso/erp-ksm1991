from django.db import models

from stocks.models import Stock, StockOrder


class PurchaseStatus(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    request_date = models.DateField(blank=False, null=False, auto_now=True, help_text='วันที่สร้าง')
    purchase_date = models.DateField(blank=False, null=False, help_text='วันสั่งซื้อ')
    expect_received_date = models.DateField(blank=False, null=False, help_text='วันที่คาดกว่าจะได้')
    received_date = models.DateField(blank=False, null=False, help_text='วันที่รับของ')
    expect_sending_date = models.DateField(blank=False, null=False, help_text='วันที่คาดว่าจะส่งของ')
    sending_date = models.DateField(blank=False, null=False, help_text='วันที่ส่งของ')

    status = models.ForeignKey(
        PurchaseStatus,
        on_delete=models.CASCADE,
    )

    noted = models.TextField(blank=True)


class PurchaseStock(StockOrder):
    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
    )
