from .models import Payable
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PayableSerializer, TransactionSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)


class TransactionCreateAPIView(CreateAPIView):
    serializer_class = TransactionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PayableCreateAPIView(CreateAPIView):
    serializer_class = PayableSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PayableListAPIView(ListAPIView):
    queryset = Payable.objects.all()
    serializer_class = PayableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_status', 'transaction__service_type']




