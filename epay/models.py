from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PaymentOrder(models.Model):
    paymentOrderId = models.CharField(name="PAYMENTORDERID", max_length=100)
    orderId= models.CharField(name="ORDERID",max_length=100)
    amount = models.IntegerField(name="AMOUNT")
    status = models.IntegerField(name='STATUS')
    orderTime=models.CharField(max_length=14)
