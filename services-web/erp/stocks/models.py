from django.db import models


class Stock(models.Model):
    sku = models.CharField(blank=False, null=False, max_length=200)
    name = models.CharField(blank=False, null=False, max_length=200)
    volume = models.PositiveIntegerField(blank=False, null=False)
    unit = models.CharField(blank=False, null=False, max_length=200)
    size = models.CharField(blank=False, null=False, max_length=200)
    brand = models.CharField(blank=False, null=False, max_length=200)
    color = models.CharField(blank=False, null=False, max_length=200)
    created_date = models.DateTimeField(blank=False, null=False, auto_now=True)
