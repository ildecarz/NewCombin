from django.db import models
from django.utils import timezone
from django.core.files import File

import barcode
from barcode.writer import ImageWriter
from io import BytesIO


class Transaction(models.Model):
    SERVICE_TYPE = (
        ('ELECTRICITY', 'ELECTRICITY'),
        ('WATER', 'WATER'),
        ('GAS', 'GAS'),
        ('INTERNET', 'INTERNET'),
        ('TV', 'TV')
    )
    service_type = models.CharField(
        max_length = 100,
        choices = SERVICE_TYPE,
        blank=False,
        null=False
    )
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    barcode = models.ImageField(upload_to='images/', blank=True, null=True)
    barcode_id = models.CharField(
        max_length = 12,
        unique = True,
        blank=False,
        null=False,
        help_text='Barcode id most be 12 digits long'
    )


    def __str__(self):
        return self.service_type

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode('ean13')
        ean = EAN(self.barcode_id, writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)


class Payable(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    PAY_METHOD = (
        ('DEBIT_CARD', 'DEBIT_CARD'),
        ('CREDIT_CARD', 'CREDIT_CARD'),
        ('CASH', 'CASH'),
    )
    transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    payment_status = models.CharField(max_length = 100, choices = STATUS)
    payment_method = models.CharField(max_length = 100, choices = PAY_METHOD)
    payment_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    card_number = models.CharField(max_length = 100, blank=True, null=True)
    payment_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.status
    
