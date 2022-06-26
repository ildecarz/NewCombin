from django.urls import path
from .views import (
    TransactionCreateAPIView,
    PayableListAPIView,
    PayableCreateAPIView
)

urlpatterns = [
    path('create-tax/', TransactionCreateAPIView.as_view(), name='create-tax'),
    path('pay-tax/', PayableCreateAPIView.as_view(), name='pay-tax'),
    path('payables/', PayableListAPIView.as_view(), name='payable-list'),
]