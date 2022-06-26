from django.test import TestCase
from .models import Transaction, Payable

# Create your tests here.

class TransactionTest(TestCase):
    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            service_type='ELECTRICITY',
            amount=100,
            description='test transaction',
            barcode_id='123456789012',
        )
        self.assertEqual(transaction.service_type, 'ELECTRICITY')
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.description, 'test transaction')
        self.assertEqual(transaction.barcode_id, '123456789012')



class TaxPayableTest(TestCase):
    def test_pay_transaction(self):
        transaction = Transaction.objects.create(
            service_type='ELECTRICITY',
            amount=100,
            description='test transaction',
            barcode_id='123456789012',
        )
        payable = Payable.objects.create(
            transaction=transaction,
            payment_status='Pending',
            payment_method='CASH',
            payment_amount=100,
        )
        self.assertEqual(payable.payment_status, 'Pending')
        self.assertEqual(payable.payment_method, 'CASH')
        self.assertEqual(payable.payment_amount, 100)

