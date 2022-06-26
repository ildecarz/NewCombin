from .models import Transaction, Payable
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = '__all__'
