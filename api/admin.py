from django.contrib import admin
from .models import Transaction, Payable

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Payable)
